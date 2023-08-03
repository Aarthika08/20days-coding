def fact(n):
    #return fact(n)*fact(n-1)
    s=n
    #for i in range(n,1,-1):
        # s*=i
    if s == 0:
        return 1

    return s*fact(n-1)    


n=int(input())
f=fact(n)
print(f)
