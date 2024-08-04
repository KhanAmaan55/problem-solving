"""
Question : https://www.hackerrank.com/challenges/designer-door-mat/problem
Done
"""

pattern = '.|.'
welcome='WELCOME'
n, m = map(int ,input().split())
for i in range(n):
    if i == int(n/2):
        print(welcome.center(m,'-'))
    elif i < int(n/2):
        print((pattern * ((2*i)+1)).center(m,'-'))
    if i > int(n/2):
        print((pattern * (2*(n-i-1) +1)).center(m,'-'))