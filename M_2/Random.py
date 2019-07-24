''' divisible by 3 and 6 but not on 9 values in random values'''
import random as rn
lst=[]
lst_1=[]
for i in range(1,100):
    lst.append(rn.randint(1,1000))
for num in lst:
    if num%3==0 and num%6 ==0 and num%9 !=0:
        lst_1.append(num)
print(lst_1)

