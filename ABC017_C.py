import io
import sys

_INPUT = """\
6
4 6
1 3 30
2 3 40
3 6 25
6 6 10
2 7
1 3 90
5 7 90
1 4
1 4 70
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  ans=[0]*(M+1)
  for i in range(N):
    l,r,s=map(int,input().split())
    l-=1
    if l>0:
      ans[0]+=s
      ans[l]-=s
    if r<M:
      ans[r]+=s
      ans[-1]-=s
  aans=[ans[0]]
  for i in range(M):
    aans.append(aans[-1]+ans[i+1])
  print(max(aans))