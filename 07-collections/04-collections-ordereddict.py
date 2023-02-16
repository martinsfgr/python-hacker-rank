from collections import OrderedDict

N = int(input())
d = OrderedDict()

for i in range(N):
    item = input().split()
    item_name = " ".join(item[:-1])
    net_price = int(item[-1])

    if item_name in d:
        d[item_name] += net_price
    else:
        d[item_name] = net_price

for item in d.items():
    print(*item)
