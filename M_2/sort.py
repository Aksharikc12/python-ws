'''print the name which starts from A and ends with H'''

data = "Rajesh,krish,manoj,suresh,jayesh,mahesh,charan,anu,anish"
print(data)
names = data.upper().split(",")
print(names)

lst=[]
for name in names:
    if name.startswith("A") or name.endswith("H"):
        lst.append(name)
lst.sort()
print(lst)
