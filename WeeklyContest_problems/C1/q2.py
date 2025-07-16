'''Chef Bakes Cake 2
Chef is an expert baker. To make a cake, he needs N different ingredients numbered 1,2,…,N. He needs Ai
amount of the ingredient numbered i, and he currently has Bi
amount of that ingredient already.
 Each ingredient costs him 1 coin to buy. Find the total cost of buying the excess ingredients necessary to make 
1 cake.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains a single integer 
N - the total number of ingredients.
The second line contains N integers - 
A1,A2,…,AN
The third line contains N integers - 
B1,B2,…,BN
Output Format
For each test case, output on a new line the total cost of buying the necessary ingredients for 
1 cake.'''


t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split(" ",n-1)))
    b=list(map(int,input().split(" ",n-1)))
    i=0
    cost=0
    for i in range(n):
        req=a[i]-b[i]
        if a[i]<b[i]:
            cost+=0
        else:
            cost+=req
        i+=1
    print(cost)    
    t-=1    
    