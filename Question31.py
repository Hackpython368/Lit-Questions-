def calculateNpowN(n):
    ans = 1
    for _ in range(n):
        ans *=n 
    return ans

if __name__=="__main__":
    n = int(input("Enter a Number :"))
    print(f"calulate {n}^{n} : {calculateNpowN(n)}")