'''9.	Write a program to accept a five-digit number, increment each digit by 1 and then display the new number formed. Note that digit 9 gets incremented to 0.
Example:
Input: 14389
Output: 25490
'''
inp = input("enter the five-digit number")
sum = 0
for num in inp:
    if num == 9:
        sum = 0
        print(sum)
    else:
        sum = int(num)+1
        print(sum,end='')