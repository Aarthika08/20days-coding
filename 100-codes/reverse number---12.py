n=int(input())
f=0
r=0

while(n>0):
    #n=str(n)
    #k=n[::-1]
    r=n%10
    f=f*10+r
    n=n//10
print(f)
    
