'''Chef Bakes Cake 1
Chef is an expert baker. Each cake costs him 
30
30 coins to make, and then he sells each for 
50
50 coins.

Today, Chef made a total of 
N
N cakes and was able to sell 
M
M cakes. The remaining cakes went unsold and were wasted.

Find out how much money (in coins) Chef made from these cakes. It may be possible that the answer is negative to indicate Chef lost money.

Input Format
The only line of input contains 
2
2 integers - 
N
N and 
M
M.
Output Format
For each test case, output on a new line the amount of money Chef made.'''

N,M=map(int,input().split(" "))
made=30*N
sold=50*M
money=sold-made
print(money)