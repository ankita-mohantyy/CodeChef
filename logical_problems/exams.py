'''Exams
In Chefland, there are 
X
X schools, and each school has 
Y
Y students.
The year end results are in and a total of 
Z
Z students passed the exams.

Assuming that all students appeared for the exams, find whether the number of students who passed in Chefland was strictly greater than 
50
%
50%.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of three space-separated integers 
X
,
Y
,
X,Y, and 
Z
Z, as mentioned in the statement.
Output Format
For each test case, output on a new line, YES, if the total number of students who passed in Chefland was strictly greater than 
50
%
50%, otherwise print NO.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).'''


t=int(input())
while t>0:
    x,y,z=map(int,input().split(" "))
    pp=((z)/(x*y))*100
    if pp>50:
        print("YES")
    else:
        print("NO")
    t-=1    