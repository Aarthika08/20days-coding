#leap year--8
n=int(input())
if n%4==0 or( n%400==0 and n%100!=0):
    print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")
