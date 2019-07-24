'''4.	Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels. (Hint: Use filter method.)
Example:
Input: quintessential
Output: ['u', 'i', 'e', 'e', 'i', 'a']; 6
'''
name = input("enter your name : ")
lst = ['a','e','i','o','u']
c = 0
lst_1 = []
for n in name:
    if n in lst: 
        lst_1.append(n)
print(lst_1)
print(len(list(filter(lambda x:x in lst , name))))