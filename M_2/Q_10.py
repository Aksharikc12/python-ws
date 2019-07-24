"""10.	Write a program to count the number of unique words and the number of occurrences of each of those words from the question provided below.
Input:
"How much wood would a woodchuck chuck if the woodchuck could chuck wood?"
Output:
Number of unique words: x
abcd: p times
efgh: q times
rstu: t times"""

data="How much wood would a woodchuck chuck if the woodchuck could chuck wood"
lst=[]
lst=data.split(" ")

c_words={}
for word in lst:
    if c_words.get(word)==None:
        c_words[word]=1
    else:
        c_words[word]+=1

count=0
for k,v in c_words.items():
    if v == 1:
        count+=1
    elif not v <2:
        print(k,":",v," times")

print("Number of unique words:",count)
