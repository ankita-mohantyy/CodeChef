'''Failing Grades
Chef took 
N
N total tests in his university, numbered 
1
1 to 
N
N chronologically. Each was graded out of 
100
100 marks. He scored 
A
i
A 
i
​
  marks in the 
i
i-th test.

Chef's scholarship requires that his average remains at or above 
40
40 marks after taking each test. Was Chef able to keep his scholarship? Print Yes or No accordingly.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains 
N
N - the number of tests.
The second line contains 
N
N integers - 
A
1
,
A
2
,
…
,
A
N
A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 .
Output Format
For each test case, output on a new line 
Yes
Yes if Chef was able to keep his scholarship and 
No
No otherwise.

It is allowed to print each character in either case, i.e. 
YES
YES, 
yes
yes, 
yES
yES will all be accepted as a positive response.

'''

t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    total = 0
    scholarship = True
    
    for i in range(n):
        total += a[i]
        average = total / (i + 1)
        if average < 40:
            print("No")
            scholarship = False
            break
    
    if scholarship:
        print("Yes")
        
    t-=1