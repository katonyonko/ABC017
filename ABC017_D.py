import io
import sys

_INPUT = """\
6
5 2
1
2
1
2
2
6 6
1
2
3
4
5
6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  N,M=map(int,input().split())
  F=[int(input())-1 for _ in range(N)]
  dp=[0]*(N+1)
  adp=[0]*(N+2)
  dp[0]=1
  adp[1]=1
  l=0
  tmp=[0]*M
  for i in range(N):
    tmp[F[i]]+=1
    while tmp[F[i]]==2:
      tmp[F[l]]-=1
      l+=1
    dp[i+1]=(adp[i+1]-adp[l])%mod
    adp[i+2]=(adp[i+1]+dp[i+1])%mod
  print(dp[-1])