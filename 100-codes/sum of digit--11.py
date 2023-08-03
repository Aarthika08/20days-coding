n=int(input())
f=0
r=0

for i in range(n):
    #r=n%10
    f=f+n%10
    n=n//10
    
print(f)
	
	
