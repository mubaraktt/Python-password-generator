from random import *

ch1="abcdefghijklmnopqrstuvwxyz"
ch2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
no1="1234567890"
p1="!@#$%&*+"
password=ch1+ch2+no1+p1
characters="".join(choice(password)for x in range(randint(8,16)))
print(characters)
