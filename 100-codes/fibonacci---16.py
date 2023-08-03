n=int(input())
a=0
b=1
s=0
for i in range(n):
    a=b
    b=s
    print(s)
    s=a+b

    
