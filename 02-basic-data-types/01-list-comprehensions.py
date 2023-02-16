if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i_arr = [x for x in range(0, x+1)]
    j_arr = [y for y in range(0, y+1)]
    k_arr = [z for z in range(0, z+1)]

    all_permutations = [[i, j, k] for i in i_arr for j in j_arr for k in k_arr]
    validated_permutations = [x for x in all_permutations if sum(x) != n]
    print(validated_permutations)
