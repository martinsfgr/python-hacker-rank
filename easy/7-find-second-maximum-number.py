if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    no_repeats_arr = sorted(set(arr), reverse=True)

    print(no_repeats_arr[1])
    