#what is the expected output of the following Python code given below-

data=[10, 501, 22, 37, 100, 999, 87, 351]
result=filter (lambda x: x>4, data)
print(list(result))

#Write a Python code using Lambda function to check every element of a List is an Integer or String

List= [10, "END", 100, 200, "T", [ ]]
x= lambda x: isinstance(x, (int, str))
all_elements = all(map(x, List))
print("All elements are either integers or strings:", all_elements)


#Write a Python function to validate the Regular Expression for the following-
#a)Email address
import re

def valid_email(email):
    pattern_email = r'^[A-Za-z0-9_]+\.?+@[A-Za-z0-9.]+\.[A-Za-z]{2,}$'

    if re.match(pattern_email, email):
        return True
    else:
        return False

data1 = ["user@gmail.com", "user@.com."]

for email in data1:
    if valid_email(email):
        print(f"{email} is a valid email address")
    else:
        print(f"{email} is NOT a valid email address")

#b) Mobile numbers of Bangladesh

def valid_bangladesh_num(number):
    pattern_number=r'\+880 \d{3} \d{3} \d{4}'

    if re.match(pattern_number,number):
        return True
    else:
        return False

Data2= ['+880 654 356 8765','001 323 222 1', '227 733 333 77777 733']

for number in Data2:
    if valid_bangladesh_num(number):
        print(f"{number} is valid bangladesh number")
    else:
        print(f"{number} is invalid bangladesh number")

#c) Telephone number of USA

def valid_USA_num(number):
    pattern_number=r'\+1\d{3} \d{3} \d{4}'

    if re.match(pattern_number,number):
        return True
    else:
        return False

Data2= ['+1880 654 3568','001 323 222 1', '+1543 654 3568']

for number in Data2:
    if valid_USA_num(number):
        print(f"{number} is valid USA number")
    else:
        print(f"{number} is invalid USA number")

#d) 16 character Alpha numeric password composed of alphabets of Upper Case Lower Case , Sepecial characters, Numbbers

def valid_password(password):
    pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{16}$'

    if re.match(pattern_password,password):
        return True
    else:
        return False
data3=['ggfffd1', 'Auytr!#$$R1s2f#y', 'frwe']

for password in data3:
    if valid_password(password):
        print(f'{password} is valid')
    else:
        print(f'{password} is invalid')







