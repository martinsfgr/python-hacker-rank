string = input()
string_capitalized = string.split()

for word in string_capitalized:
    string = string.replace(word, word.capitalize())

print(string)
