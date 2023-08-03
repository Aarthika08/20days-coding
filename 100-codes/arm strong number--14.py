n=int(input())
f=0
r=0
t=n
l=len(str(n))
while(n>0):
    #n=str(n)
    #k=n[::-1]
    r=n%10
    n=n//10
    f=f+pow(r,l)

print(f)
if f==t:print('yes')
else:print('No')
