'''Chef and Candies
There are N children and Chef wants to give them 1 candy each. Chef already has X candies with him. To buy the rest, he visits a candy shop. In the shop, packets containing exactly 4 candies are available.

Determine the minimum number of candy packets Chef must buy so that he is able to give 1 candy to each of the N children.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
The first and only line of each test case contains two integers N and X — the number of children and the number of candies Chef already has.
Output Format
For each test case, output the minimum number of candy packets Chef must buy so that he is able to give 1 candy to each of the N children.'''

t=int(input())
while t>0:
    n,x=map(int,input().split(" "))
    req=n-x
    if n<x:
        print(0)
    else:
        if req%4!=0:
            print((req//4)+1)
        elif req%4==0:
            print(req//4)    
    t-=1