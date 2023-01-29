N = int(input())
M = N*3

center = N // 2
output = []


for i in range(N):
    if i == center:
        line_to_print = "WELCOME".center(M, "-")
        output.append(line_to_print)

    elif i > center:
        line_to_print = output[:center]
        line_to_print.reverse()

        for j in line_to_print:
            output.append(j)
        break

    else:
        line_to_print = (".|." * (i * 2 + 1)).center(M, "-")
        output.append(line_to_print)
    

for line in output:
    print(line)
