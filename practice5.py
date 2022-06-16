#5. Write a Python program to find uncommon words from two Strings?
str1 = 'hello'
str2 = 'byebro'
str3 = []
for i in str1:
    if i not in str2:
        if i not in str3:
            str3.append(i)
for i in str2:
    if i not in str1:
        if i not in str3:
            str3.append(i)
print(str3)