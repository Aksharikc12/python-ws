'''7.	Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number.'''

inp = input("enter the number :")
sum = 0
for num in inp:
    sum += int(num)
print(sum)