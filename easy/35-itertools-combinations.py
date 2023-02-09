from itertools import combinations

S, K = input().split()

for i in range(int(K)):
    all_combinations = list(combinations(sorted(S), i+1))

    for j in all_combinations:
        print("".join(j))
