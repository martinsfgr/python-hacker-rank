from itertools import combinations_with_replacement

S, k = input().split()
combinations = combinations_with_replacement(sorted(S), int(k))

for i in combinations:
    print("".join(i))
