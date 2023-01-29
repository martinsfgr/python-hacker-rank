size = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

output = []
j = size - 1

for i in range(size + 1):
    if i == size:
        for k in output[::-1][1:]:
            output.append(k)

    else:
        strip = "-".join(list(alphabet[j:size]))

        if len(strip) > 1:
            output.append(strip[1:][::-1] + strip)
        else:
            output.append(strip)
        j -= 1

width = len(output[len(output) // 2])

for line in output:
    print(line.center(width, "-"))
