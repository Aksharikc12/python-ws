'''9.	Write a program to find the word(s) that occur maximum and minimum number of times in the given paragraph. Also, display those words next to their respective count.'''
inp="Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3."""
lst=[]
lst_1=[]
c_words={}
lst=inp.split(" ")
for word in lst:
    if c_words.get(word)==None:
        c_words[word]=1
    else:
        c_words[word]+=1

lst_1=[v for v in c_words.values()]
max=lst_1[0]
min=lst_1[0]
for i in lst_1:
    if i<min:
        min=i 
    elif i>max:
        max=i

for k,v in c_words.items():
    if v ==max:
        print(k,":",v)
    elif v==min:
        print(k,":",v)
        
