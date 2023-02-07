T = int(input())

for i in range(T):
    a, b = input().split()
    
    try:
        print(f"{int(a) / int(b):.0f}")

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)
