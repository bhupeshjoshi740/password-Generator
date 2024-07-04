import random
import string

print("Welcome to password generator")

lower=string.ascii_lowercase 
upper=string.ascii_uppercase
digits=string.digits
symbol=string.punctuation 

all=lower+upper+digits+symbol
length=int(input("Enter the length of password:"))

password=random.sample(all,length)
password="".join(password)

print("password is:",password)

salary = 900
new_salary = salary + 200
print(new_salary)