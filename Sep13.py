# WAP to print cube of first n numbers
def printCube(n):
    for i in range(1,n+1):
        print(i**3,end="  ")

# WAP to rotate an array.
def rotateArray(lst :list,n :int):
    for i in range(n):
        lst[i],lst[len(lst)-i-1] = lst[len(lst)-i-1],lst[i]
        print(lst)

# WAP to sort word in alphabetical order
def sortInAlpha(word :str):
    s = list(word)
    s.sort()
    newWord = ""
    for i in s:
        newWord += i
    return newWord

#WAP to print first n pronic Number
def printnPronic(n :int):
    for i in range(1,n+1):
        print(i*(i+1),end="  ")
    

# WAP to multiply all the element of the lst
def mulList(lst :list):
    product = 1
    for i in lst:
        product *= i
    
    return product


# WAP to clone a lst
def cloneLst(lst :list):
    return lst.copy()




