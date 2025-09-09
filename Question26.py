b = 4
s = b - 1
count = 0
for i in range(7):
    print(s*" "+b*"*",end=" \n")
    if count==3:
        s -= 1
        b+=1
    else:
        count += 1
        b-=1

n = int(input("Enter a number :"))
s = n-1
for i in range(n):
    print(s*" "+n*"*")
    n -= 1