# here is the print statement
# print("Hello World")

# here is the variable
temp = 0.12
myStr = "Hello Ayaan"
myBool= True
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
           


makePyramid(10)