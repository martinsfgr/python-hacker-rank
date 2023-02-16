def print_formatted(number):
    pad = len(f"{number:b}")

    for i in range(1, number+1):
        print(f"{i:d}".rjust(pad), f"{i:o}".rjust(pad), f"{i:X}".rjust(pad), f"{i:b}".rjust(pad))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    