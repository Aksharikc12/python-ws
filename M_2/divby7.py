import random as rn
nums=[ rn.randint(100,500) for i in range(100,500) if i%7 == 0 ]
print(nums)