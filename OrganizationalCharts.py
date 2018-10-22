import sys

#m_file = open("org_chart_in2.txt","r")

firstline = sys.stdin.readline().strip()
N = int(firstline.split(" ")[0])
Q = int(firstline.split(" ")[1])

node_list = {}
root = None
sys.setrecursionlimit(100000)

class Node:
		def __init__(self,par_name,name,div_size,all_size):
			self.par_name = par_name
			self.par = None
			self.name = name


			self.div_size = div_size
			self.all_size = all_size

			self.div_min = div_size
			self.div_max = div_size

			self.all_min = all_size
			self.all_max = all_size

			if div_size == 0:
					self.unknown_div_max = True
					self.unknown_div_min = True
			else:
					self.unknown_div_max = False
					self.unknown_div_min = False

			if all_size == 0:
					self.unknown_all_max = True
					self.unknown_all_min = True
			else:
					self.unknown_all_max = False
					self.unknown_all_min = False

			self.children = []
			self.depth = 0

		def set_par(self, par):
			if par is not None:
					self.par = par
					par.children.append(self)

		def set_depth(self):
			for child in self.children:
				child.depth = self.depth + 1
				child.set_depth()


		def prime_node(self):
				if len(self.children) == 0 and (self.div_size != 0 or self.all_size != 0):
						if self.div_size == 0 and self.all_size != 0:
								self.div_size = self.all_size
						elif self.div_size != 0 and self.all_size == 0:
								self.all_size = self.div_size
						return

				if self.div_size == 0:
						self.div_min = 1
						self.div_max = float("inf")

				if self.all_size == 0:
						self.all_min = 1
						self.all_max = float("inf")

						for child in self.children:
								self.all_min += child.all_min

		def get_div_max(self):
				if self.unknown_div_max:
						ch_all_min = sum([x.all_min for x in self.children])
						self.div_max = self.get_all_max() - ch_all_min
						self.unknown_div_max = False
				return self.div_max

		def get_div_min(self):
				if self.unknown_div_min:
						ch_all_max = sum([x.all_max for x in self.children])
						ret_val = self.get_all_min() - ch_all_max
						self.div_min = ret_val if ret_val > 0 else 1
						self.unknown_div_min = False
				return self.div_min

		def get_all_max(self):
				if self.unknown_all_max:
						sib_all_min = sum([x.get_all_min() for x in self.par.children if x != self])
						self.all_max = self.par.get_all_max() - self.par.get_div_min() - sib_all_min
						self.unknown_all_max = False
				return self.all_max

		def get_all_min(self):
				if self.unknown_all_min:
						sib_all_max = sum([x.get_all_max() for x in self.par.children if x != self])
						ret_val =  self.par.get_all_min() - self.par.get_div_max() - sib_all_max
						self.all_min = ret_val if ret_val > 0 else 1
						self.unknown_all_min = False
				return self.all_min


		def find_ranges(self):
				self.get_div_min()
				self.get_div_max()








unknown_nodes = []

for i in range(N):
		line = sys.stdin.readline().strip().split(" ")
		div_name = line[0]
		par_name = line[1]
		div_size = int(line[2])
		all_size = int(line[3])

		if par_name == "NONE":
				new_node = Node(None,div_name,div_size,all_size)
				root = new_node
		else:
				new_node = Node(par_name,div_name,div_size,all_size)

		node_list[div_name] = new_node

		if div_size == 0 or all_size == 0:
				unknown_nodes.append((new_node.depth,new_node))

for node_name in node_list:
	node = node_list[node_name]
	if node == root:
		continue
	node.set_par(node_list[node.par_name])

root.set_depth()


# SORT unknown_nodes
unknown_nodes.sort(key=lambda tup: tup[0], reverse = True)





working_nodes = [] # Nodes at lowest level

while len(unknown_nodes) > 0:
		current_depth = unknown_nodes[0][0]
		while len(unknown_nodes) > 0 and unknown_nodes[0][0] == current_depth:
				this_node = unknown_nodes[0][1]
				if not (this_node.unknown_all_min or this_node.unknown_all_max or this_node.unknown_div_max or this_node.unknown_div_min):
					del unknown_nodes[0]
					continue
				working_nodes.append(this_node)
				del unknown_nodes[0]

		for node in working_nodes:
				node.prime_node()
		for node in working_nodes:
				node.find_ranges()
		working_nodes = []

for i in range(Q):
	line = sys.stdin.readline().strip().split(" ")
	division = line[0]
	type = int(line[1])
	if type == 1:
		print(str(node_list[division].div_min) + " " + str(node_list[division].div_max))
	else:
		print(str(node_list[division].all_min) + " " + str(node_list[division].all_max))
