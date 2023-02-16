if __name__ == '__main__':
    N = int(input())
    L = []
    
    for i in range(N):
        operation = input()
        
        if operation.startswith("insert"):
            operation = operation.split()
            L.insert(int(operation[1]), int(operation[2]))

        elif operation.startswith("print"):
            print(L)

        elif operation.startswith("remove"):
            operation = operation.split()
            L.remove(int(operation[1]))

        elif operation.startswith("append"):
            operation = operation.split()
            L.append(int(operation[1]))

        elif operation.startswith("sort"):
            L.sort()

        elif operation.startswith("pop"):   
            L.pop()

        elif operation.startswith("reverse"):
            L.reverse()
