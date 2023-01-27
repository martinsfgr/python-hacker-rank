def swap_case(s):
    transformed_string = ""

    for i in s:
        if i.isupper():
            transformed_string = transformed_string + i.lower()
        else:
            transformed_string = transformed_string + i.upper()

    return transformed_string


if __name__ == '__main__':
   s = input()
   result = swap_case(s)
   print(result)
