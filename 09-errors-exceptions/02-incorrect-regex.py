import re

T = int(input())
inputs = [input() for _ in range(T)]

for input in inputs:
    try:
        re.compile(input)
        print("True")
    except:
        print("False")
