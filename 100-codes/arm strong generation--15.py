import math
first=150
last=10000
def is_Armstrong(val):
    s=0
    arr=[int(d) for d in str(val)]
    for i in range(0,len(arr)):
        s+=pow(arr[i],len(arr))

    if s == val:
        print(str(val) + ", ", end="")        
for i in range(first, last + 1):
    is_Armstrong(i)
