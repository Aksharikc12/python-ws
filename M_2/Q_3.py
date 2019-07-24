'''3.	Write a program to determine the work hours of the day entered based on the timetable provided below.

Mon	Tue	Wed	Thu	Fri	Sat	Sun
3	3	3	3	3	3	0
2	2	2	2	2	1	0
2	2	2	1	1	0	0
'''
dic ={'mon' : [3,2,2],"tue" : [3,2,2],'wed' : [3,2,2],'thu' : [3,2,1],'fri' : [3,2,1],'sat' : [3,1,0],'sun' : [0,0,0] }
day = input("enter the day: ")
for k,v in dic.items():
    if day == k:
        print(f"{k} = {v}")

