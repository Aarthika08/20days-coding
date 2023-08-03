n=int(input())
f=0
r=0
t=n
while(t>0):
    #n=str(n)
    #k=n[::-1]
    r=t%10
    f=f*10+r
    t=t//10
print(f)
if f==n:
    print('PALINDROME NUMBER')
else:
     print('NOT  PALINDROME NUMBER')

    
