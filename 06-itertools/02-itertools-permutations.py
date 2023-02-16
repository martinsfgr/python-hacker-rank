from itertools import permutations

string, integer = input().split()
all_permutations = list(permutations(string, int(integer)))

for permutation in sorted(all_permutations):
    print("".join(permutation))
