#4. Write a Python to check if a given string is binary string or not?
def checkbinary(str):
    flag  = False
    for i in str:
        if i=='0' or i=='1':
            flag = True
        else:
            flag = False
            break
    return flag

while checkbinary('0101010010101'):
    print("It is binary string.")
    break
else:
    print("It is not binary string.")