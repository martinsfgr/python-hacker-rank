from collections import defaultdict

d = defaultdict(list)
n, m = input().split()

for i in range(int(n)):
    d["A"].append(input())

for i in range(int(m)):
    d["B"].append(input())

for i in d["B"]:
    if i in d["A"]:
        indexes = []

        for j in list(enumerate(d["A"])):
            if i in j:
                indexes.append(j[0])
        
        print(*[x + 1 for x in indexes])

    else:
        print(-1)
