n = 15
count = 7
b = 1
d = 0
p = 1

for i in range(n):
    if i==0 or i==14:
        print(" "*count+"*"*b)
        count -= 1
    else:
        if i>6:
            print(" "*count+"*"*b+p*" "+b*"*")
            count += 1
            p -= 2
        else:
            print(" "*count+"*"*b+p*" "+b*"*")
            count -= 1
            p += 2
    