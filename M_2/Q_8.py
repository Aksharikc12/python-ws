"""Write a function which implements the Pascal's triangle."""
lst=[[1],[1,1]]
for i in range(3,8):
    lst1=[1]
    for j in range(len(lst[len(lst)-1])-1):
        lst1.append(lst[i-2][j]+lst[i-2][j+1])
    lst1.append(1)
    lst.append(lst1)
for i in range(len(lst)):
    res=""
    for j in range(len(lst)-i):
        res+=" "
    if i>5:
        res=res[i-3]
    print(res,end="")
    for j in lst[i]:
        print(j,end=" ")
    print()
