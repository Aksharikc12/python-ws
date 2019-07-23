'''3.	Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.'''

import math
def is_prime(num):
    
    is_prime=True
    if num<2:
        is_prime=False
    else:
        for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0:
                 is_prime=False
                 break
    if is_prime:
        print(num)

lb=int(input("enter the lower bound number"))
ub=int(input("enter the upper bound number"))
for i in range(lb,ub+1):
    is_prime(i)