'''2.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1 + 1/2 + 1/3 + ……. + 1/n
'''
import math
sum=0
n=int(input("enter the upper bound number"))
for i in range(1,n+1):
    sum=sum+(1/i)
print(sum)