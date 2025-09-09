n = int(input("Enter a number :"))
count = 1
for i in range(n):
    print(n*" "+count*"*")
    count += 1
    n -= 1
