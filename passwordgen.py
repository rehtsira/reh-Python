import random
import string

up = string.ascii_uppercase
low = string.ascii_lowercase
num = string.digits
sym = string.punctuation

pwdlist = up + low + num + sym

length = input("How many characters do you want your password to be?\n")

p = ''.join(random.choices(pwdlist,k=int(length)))

print(p)
