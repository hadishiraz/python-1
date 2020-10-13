
#function to multiply any number of digits
def multi(*q):
    res=1
    temp=0
    for temp in q:
        res= res*temp
    return res

x=multi(10.2,10,7)
print(x)
x=multi(3,10,7,90,4)
print(x)
x=multi(10)
print(x)

#add n to 0 serie
def recursionAdd(k):
    if(k > 0):
        result = k + recursionAdd(k - 1)
        print("k="+str(k)+" res= " +str(result))
    else:
        result = 0 #this acctualy is the init of result var when func come down 
        print("k="+str(k)+" res= " +str(result))
    return result

print("\n\nRecursion Example Results")
recursionAdd(5)