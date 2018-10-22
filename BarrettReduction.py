import sys
# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

a = get_number()
b = get_number()
found = False
low = 0
high = 2**31
while not found:
#def findIt(low, high):
    mid = (low + high) >> 1
    result = mid * a >> b
    if result == 0:
        low = mid
        continue
    elif result >= 2:
        high = mid
        continue
    else: # result == 1
        result2 = (mid - 1) * a >> b
        if result2 == 0:
            found = True
            break
        else:
            high = mid
            continue

upper = mid
#for i in range(upper + 1, 0, -1):
#result = i * a >> b
#if result == 0:
#    print(i + 1)
#else
#    a = 1/0
print(mid)

