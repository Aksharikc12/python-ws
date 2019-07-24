name = input("enter your name : ")
lst = ['a','e','i','o','u']
c = 0
for n in name:
    if n in lst: 
        c+=1
print(c)



print(len(list(filter(lambda x:x in lst , list(name)))))


print(len(list(filter(lambda x:x in lst , name))))