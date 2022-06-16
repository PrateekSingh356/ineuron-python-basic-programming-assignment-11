#3. Write a Python program to split and join a string?
str = 'hello how are you.'
print(f"before splitting: {str}")
def splitting(str):
    str1 = str.split(" ")
    return str1

print(f"after splitting: {splitting(str)}")
def joining(str1):
    for i in str1:
        str2 = str+i
        return str2
print(f"after joining: {joining(str)}")
