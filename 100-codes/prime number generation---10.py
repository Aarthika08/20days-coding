#prime number generation--10
n=int(input())
h=int(input())
f=0
for i in range(n,h):
    if i==2 or i==3 :print(i)
    if i%2==0 or  i%3==0 :
        f=1
    else:
        print(i)
