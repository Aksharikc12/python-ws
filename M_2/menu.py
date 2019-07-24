lst = []
def add(ele):
    lst.append(ele)
def pop():
    if len(lst) == 0:
        print("list empty")
    else:
        ele=lst.pop()
        print(f"element {ele} removed")
def search(ele):
    if len(lst) == 0:
        print("empty")
    else:
        if ele in lst:
            index=lst.index(ele)
            print(f"{ele} is found in {index}")
        else:
            print(f"given {ele} not found")
def display():
     if len(lst) == 0:
        print("list empty")
     else:
        print(lst)
    

while True:
    print("\n**** 1.Add 2.Delete 3.search 4.display 5.exit ****")
    ch=int(input("enter the choice"))
    if ch == 1:
        ele = int(input("enter the element to add"))
        add(ele)
    elif ch == 2:
        pop()
    elif ch == 3:
        ele=int(input("enter the element to search"))
        search(ele)
    elif ch == 4:
        display()
    else:
        print("Thank you..............")
        break

