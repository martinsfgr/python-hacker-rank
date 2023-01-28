if __name__ == '__main__':
    s = input()
    
    is_alphanumeric = False
    is_alphabetical = False
    is_digit = False
    is_lower = False
    is_upper = False
    
    for x in s:
        if x.isalnum():
            is_alphanumeric = True

    for x in s:
        if x.isalpha():
            is_alphabetical = True
    
    
    for x in s:
        if x.isdigit():
            is_digit = True
            
    for x in s:
        if x.islower():
            is_lower = True
            
    for x in s:
        if x.isupper():
            is_upper = True
    
    print(is_alphanumeric)
    print(is_alphabetical)
    print(is_digit)
    print(is_lower)
    print(is_upper)
