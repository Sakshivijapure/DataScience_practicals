numbers=[10,35,4,5,12]
print(numbers[1])

def printNumbers(n):
    for i in n:
        print(i)
printNumbers(numbers)

def printNum(n):
    for i in n:
        if((i%2)==0):
            print(i)
print(printNum(numbers))

def printNumber(n):
    sum=0
    for i in n:
        if((i%2)==0):
            sum=sum+i
        return sum
print(printNumber(numbers))

name="kushwanth singh"
def printItems(n):
    for i in n:
        print(i)
printItems(numbers)
printItems(name)

def printItems(m):
    index=0
    while(index<len(m)):
        print(m[index])
        index=index+1
printItems(name)

def printItems(m):
    index=len(m)-1
    while(index>=0):
        print(m[index],end="|")
        index=index-1
    print()
printItems(name)

