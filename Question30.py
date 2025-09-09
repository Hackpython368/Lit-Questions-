def printFibonacci(n):
    i = 1
    j = 1
    print(i,j ,end=" ")
    for k in range(n-2):
        print(i+j,end=" ")
        i = j
        j = i+j


if __name__=="__main__":
    n = int(input("Enter a Number :"))
    printFibonacci(n)