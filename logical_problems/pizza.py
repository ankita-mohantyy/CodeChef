'''Minimum Pizzas
Each pizza consists of 
4
4 slices. There are 
N
N friends and each friend needs exactly 
X
X slices.

Find the minimum number of pizzas they should order to satisfy their appetite.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two integers 
N
N and 
X
X, the number of friends and the number of slices each friend wants respectively.
Output Format
For each test case, output the minimum number of pizzas required.'''

t=int(input())
while t>0:
    n,x=map(int,input().split(" "))
    if (n*x)%4!=0:
        print(((n*x)//4)+1)
    else:    
        print((n*x)//4)
    t-=1
