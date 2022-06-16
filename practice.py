#7. Write a Python Program to check if a string contains any special character?
import re
def check_splcharacter(test):
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (string_check.search(test) == None):
        print("String does not contain Special Characters.")
    else:
        print("String contains Special Characters.")
test = "hello%"
check_splcharacter(test)