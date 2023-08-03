#greatest of two number---1
n,k,l=map(int,input().split())
if n>k and n>l :
    print(n,"is greater")
elif k>n and k>l:
    print(k,"is greater")
elif l>n and l>k:
    print(l,"is greater")

else:
    print("equal")
