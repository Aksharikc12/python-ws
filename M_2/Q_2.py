'''2.	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row

Example:
Input: 
[[0 1 2 3]
 [3 4 5 5]
 [6 7 8 8]
 [9 0 1 9]]

Output:
	minimum value element in the array: 0
	maximum value element in the array: 9
	elements with minimum values column-wise: [0 0 1 3]
	elements with maximum values column-wise: [9 7 8 9]
	elements with minimum values row-wise: [0 3 6 0]
	elements with maximum values row-wise: [3 5 8 9]


'''

lst = [[0,1, 2, 3], [3, 4, 5, 5], [6, 7, 8, 8], [9, 0, 1, 9]]
lst_1=[]
for num in lst:
    lst_1.extend(num)

print(f"minimum value element in the array: {min(lst_1)}")
print(f"maximum value element in the array: {max(lst_1)}")

min_col=list(min(map(lambda x:x[i],lst)) for i in range(4))
print(f"elements with minimum values column-wise: {min_col}")
max_col=list(max(map(lambda x:x[i],lst)) for i in range(4))
print(f"elements with minimum values column-wise: {max_col}")

min_row=list(map(lambda x:min(x),lst))
print(f"elements with minimum values row-wise:{min_row}")
max_row=list(map(lambda x:max(x),lst))
print(f"elements with minimum values row-wise:{max_row}")
