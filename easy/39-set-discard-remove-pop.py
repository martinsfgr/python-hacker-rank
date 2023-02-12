n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input().split()

    if command[0].startswith("pop"):
        if len(command) == 1:
            s.pop()
        else:
            s.pop(int(command[1]))
    
    elif command[0].startswith("remove"):
        s.remove(int(command[1]))
    
    elif command[0].startswith("discard"):
        s.discard(int(command[1]))

print(sum(s))
