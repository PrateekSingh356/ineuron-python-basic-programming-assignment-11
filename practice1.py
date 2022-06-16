#1. Write a Python program to find words which are greater than given length k?
length = 5
l = ['apple', 'basket', 'happy', 'kangaroo', 'cat', 'elephant','hobby']
print("the words with length greater than 5 is: \n")
for i in l:
    if len(i)>length:
        print(i)