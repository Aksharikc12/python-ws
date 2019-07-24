'''5.	Write a program to add the elements of 2 arrays that are of the same dimension. (Hint: Use map method.)
Example:
Input:
x = [1,2,3,4]
y = [5,6,7,8]
Output: 
z = [6,8,10,12]

'''

lst_1 = [1,2,3,4]
lst_2 = [4,5,6,7]
lst_3 = list(map(lambda a,b : a+b , lst_1, lst_2))
print(lst_3)