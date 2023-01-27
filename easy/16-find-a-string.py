count = 0

def count_substring(string, sub_string):
    global count 

    if string.find(sub_string) != -1:
        count = count + 1
        index = string.find(sub_string)
        new_string = string[index+1:]
        count_substring(new_string, sub_string)
        return count
    
    return count

# FORMA ALTERNATIVA:
# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         current_string = string[i:i + len(sub_string)]
#         if current_string == sub_string:
#             count += 1
#     return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
