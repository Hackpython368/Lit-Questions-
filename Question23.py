def sumOfn(n):
    if n == 0:
        return 0
    else:
        return (n*(n+1))/2
    
    
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The sum of first {n} natural numbers is: {int(sumOfn(n))}")