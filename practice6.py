#6. Write a Python to find all duplicate characters in string?
string = "findingduplicate character"
duplicates = []
for char in string:
    if string.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)
print(*duplicates)