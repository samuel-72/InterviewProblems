#!/bin/python
def calc(n,arr):
    dp=[0 for x in range(n)]
    for i in range(0,n):
        if arr[i]==1:
            dp[i]=0
        else:
            if i==0:
                dp[i]=1000000000
            else:
                dp[i]=dp[i-1]+1
    return dp

n,m=map(int,raw_input().split())
c=map(int,raw_input().split())
flag=[0 for x in range(n)]
for val in c:
    flag[val]=1


d1=calc(n,flag)
flag=flag[::-1]
d2=calc(n,flag)
d2=d2[::-1]

print d1, d2, flag

ans=0
for i in range(n):
    ans=max(ans,min(d1[i],d2[i]))

print ans