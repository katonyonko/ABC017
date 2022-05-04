import io
import sys

_INPUT = """\
6
50 7
40 8
30 9
990 10
990 10
990 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  ans=0
  for i in range(3):
    s,e=map(int,input().split())
    ans+=s*e//10
  print(ans)