''' 4.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1/2**3 + 1/3**3 + 1/4**3 + …… + 1/n**3
'''
import math
sum=0
n=int(input("enter the upper bound number"))
for i in range(1,n+1):
    sum=sum+(1/(i**3))
print(sum)