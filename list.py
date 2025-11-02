list=["abc",2,"def",7,"ghi"]
def listItems(n):
    sumInt=0
    sumString=""
    for i in n:
        if(type(i)==int):
            sumInt=sumInt+i
        elif(type(i)==str):
            sumString=sumString+i
    print(sumInt)
    print(sumString)
listItems(list)


def listItems(n):
    sumString=""
    for i in n:
        sumString=sumString+str(i)
        print(sumString)
listItems(list)

