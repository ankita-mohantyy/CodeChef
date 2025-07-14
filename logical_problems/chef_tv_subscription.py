''' Subscriptions
A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of 
N
N friends in Chefland want to buy Chef-TV subscriptions. We know that 
6
6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is 
X
X rupees. Determine the minimum total cost that the group of 
N
N friends will incur so that everyone in the group is able to use Chef-TV.

Input Format
The first line contains a single integer 
T
T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers 
N
N and 
X
X — the size of the group of friends and the cost of one subscription.
Output Format
For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Chef-TV. '''

t=int(input())
while t>0:
    n,x=map(int,input().split())
    if n%6==0:
        money=(n//6)*x
    elif n<6:
        money=x
    elif n>6 and n%6!=0:
        money=((n//6)+1)*x
    print(money)    
    t-=1