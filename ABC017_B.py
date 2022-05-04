import io
import sys

_INPUT = """\
6
chokuou
kuccho
atcoder
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X=input()
  i=0
  ans='YES'
  while i<len(X):
    if X[i] in set(['o','k','u']): i+=1
    elif X[i]=='c':
      if i<len(X)-1 and X[i+1]=='h': i+=2
      else: ans='NO'; break
    else: ans='NO'; break
  print(ans)