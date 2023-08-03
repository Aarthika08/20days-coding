from math import sqrt

def isPerfectSquare(x):

  if x>0:
    s=int(sqrt(x))
    return s*s==x
  return false



n = int(input())
if isPerfectSquare(n):
    print("True")
else:
    print("False")
