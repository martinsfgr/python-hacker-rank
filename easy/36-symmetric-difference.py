M = int(input())
M_set = set(input().split())

N = int(input())
N_set = set(input().split())

differences = [M_set.difference(N_set), N_set.difference(M_set)]
result = []

for i in differences:
    for j in i:
        result.append(j)

for i in sorted(map(int, result)):
    print(i)
