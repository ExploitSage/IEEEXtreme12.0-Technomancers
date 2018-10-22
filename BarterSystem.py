import sys

mod_rate = 998244353

data = [line.strip('\r\n') for line in sys.stdin.readlines()]

num_commodity_rates = int(data.pop(0))  
commodity_rates = [data.pop(0).split() for i in range(0, num_commodity_rates)]

num_queries = int(data.pop(0))
queries = [data.pop(0).split() for i in range(0, num_queries)]

commodity_edges = []
exchange_rates = []

# Create Graph, Generating all missing links
for rate in commodity_rates:
    commodity_edge = (rate[0], rate[1])
    exchange_rate = int(rate[2])
    
    suppliment_edges = [commodity_edge]
    suppliment_rates = [exchange_rate]
    
    for edge in commodity_edges:
        if edge[1] == commodity_edge[0]:
            suppliment_edges.append((edge[0], commodity_edge[1]))
            suppliment_rates.append((exchange_rates[commodity_edges.index(edge)]*exchange_rate)%mod_rate)
    
    commodity_edges.extend(suppliment_edges)
    exchange_rates.extend(suppliment_rates)

for query in queries:
    if query[0] == query[1]:
        print(1)
    elif (query[0], query[1]) in commodity_edges:
        print(exchange_rates[commodity_edges.index((query[0], query[1]))])
    elif (query[1], query[0]) in commodity_edges:
        print(pow(exchange_rates[commodity_edges.index((query[1], query[0]))], mod_rate-2, mod_rate))
    else:
        print("-1")
    