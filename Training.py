# here is the print statement
# print("Hello World")

# here is the variable
temp = 0.12
myStr = "Hello Ayaan"
myBool= False
myInt = 3
myList = [1,2,3,4,5]

# string/list manipulation
# print(myList[::-2])

# string is basically a list of characters
# string[start: end]
# start index is inclusive, end index is exclusive

# for i in range(len(myList)):
#     print(i**i)

i=0
while True:
    print("Hello", i)
    i+=1
    if i>=5:
        break

# functions

def myFunction(a,b):
    temp = a+b+7
    temp=temp*a
    return temp         

temp1=myFunction(3,4)
print() # new empty line printed
print(temp1)

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def fibonacci(numberofterms):
    a=1
    b=1
    terms=[a,b]
    if numberofterms==1:
        return [a]
    elif numberofterms==2:
        return terms
    else:
        for i in range(numberofterms-2):
            nextterm=a+b
            terms.append(nextterm)
            a=b
            b=nextterm
        
        return terms    

# print(fibonacci(100))

def makePyramid(height):
    length = (2*height)-1
    # takes length of last line to be printed  
    for i in range(height):
        spline, stline = "", ""
        for _ in range(1,(2*(i+1))):
            stline = stline + "*"
        space = (length - len(stline))//2
        for _ in range(1,space+1):
            spline = spline + " "
        print(spline + stline)
           
makePyramid(25)

arr = [423,726,2,64,894,71,462,2,1,8,3434,119.45,682,245,546,111]

def bubbleSort():
    global arr # by-reference
    
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# every variable has a memory address, and the value is stored at that memory address
# in by-value, a copy of the value is passed to the function
# in by-reference, the memory address is passed to the function

bubbleSort()           

def binarySearch():
    global arr

    valuetofind = float(input("Enter the value to find: "))
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==valuetofind:
            return mid
        elif arr[mid]<valuetofind:
            start = mid+1
        else:
            end = mid-1

    return -1

# only works when the array is sorted
# print(binarySearch())    

def linearSearch():
    global arr

    valuetofind = float(input("Enter the value to find: "))
    Flag = False
    value = -1
    # write logic here
    for i in range(len(arr)):
        if arr[i] == valuetofind:
            Flag = True
            value = i
    if Flag == True:
        print("Value was found at array location :",value)
    else:
        print("Value was not found in the array")
        
linearSearch()
