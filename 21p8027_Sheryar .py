
# In[10]:


# get inputs from user for cookies, boxes , and container
cookies = int(input('Enter the total number of Cookies: '))
cookiesInBox = int(input("Enter the number of cookies in a box: "))
boxInContainer = int(input("Enter the number of cookie boxes in a Container: "))
# calculate number of boxes
box = cookies//cookiesInBox
# calculate remaining cookies (left over)
remain_cookies = cookies % cookiesInBox
# calculate number of conainters
container = box // boxInContainer
# calculate left over boxes
remain_boxes = box % boxInContainer

print("Total Boxes:",box)
print("Total Container:",container)
print("Remaining Cookies:",remain_cookies)
print("Remaining Boxes:",remain_boxes)


# In[ ]:


def compute(n,x):
#     here we will calculate factorial
    def factorial(num):
        fact = 1    
#         here we will calulate the factorial for every value of n
        for i in range(1,num+1):
            fact = fact * i
#  
        return fact
    total_sum = 0
#     it give every value until it reaches the (n)
    for i in range(n+1):
        k = factorial(i)
        total_sum += (x**i)/k
#         here we will return the total of the series
    return total_sum

number = int(input("enter number (n): "))
variable = int(input("enter variable (x): " ))
total_sum = compute(number, variable)
print(total_sum)


# In[8]:


# this program checks whether the given value is a perfect number or not
def perfect_number(value):
    total = 4
    while total > 0:
#  we will check for the factors of the value
        def factor(num):
            total_sum = 0
            for i in range(1,num):            
                if num % i == 0:
    #      sum the total number of factors of the value
                    total_sum += i
    #     return the sum of factors
            return total_sum
        total_sum = factor(value)
    #     check wheter the total_sum is equal to value or not
        if total_sum == value:
            print(value,"is a perfect number")
            total-=1
        value+=1
number = 2
perfect_number(number)


# In[ ]:


# inputs the rows form user
rows = int(input('enter number'))
counter = 0
Counter = rows
for i in range(rows,0,-1):
#     builds one side of Diamond using loops
    for j in range(i):
        print(' ',end="")
    for k in range(i,rows+1):
        print(counter,end='')
    for l in range(i,rows):
         print(counter,end="")
    counter+=1
    print()
for i in range(rows+1):
    for j in range(i):
         print(' ',end="")
    for k in range(rows,i,-1):
         print(Counter,end='')
    for l in range(i,rows+1):
         print(Counter,end="")
    Counter-=1
    print()


# In[1]:


# we will take rows from the user
rows = int(input('enter number: '))
# distribute diamond in two halfs
#     this will print upper half

for i in range(rows,0,-1):
#     first print " " til i+1 to make a space
    for j in range(i+1):
        print(" ",end="")
#         print number til the remaining rows
    for k in range(i,rows+1):
#         to get 0 and so on we will subtract total rows from i 
        print(rows-i,end=" ")
    print()
for i in range(0,rows+1):
    for j in range(i+1): 
        print(" ",end="")
    for k in range(i-1,rows):
        print(rows-i,end=" ")
    print()
        


# In[33]:


# the programs takes two matrixes from user, check if the matrixs can be multiply or not, if Yes then this will
# multiply both matrixs and give a new matrix
def matrixMult():
#     take input from user 
        rowsMat_1 = int(input("Enter the number of rows for matrix 1: "))
        columnsMat_1 = int(input("Enter the number of columns for matrix 1: "))
        rowsMat_2 = int(input("Enter the number of rows for matrix 2: "))
        columnsMat_2 = int(input("Enter the number of columns for matrix 2: "))
        print("<---------------------------------------------------------------->")
#         checking that rows and column are equal or not of first and second matrix
        if rowsMat_1 == columnsMat_2:
            matrix_1 = []
            matrix_2 = []
            matrix_3 = []
            for i in range(rowsMat_1):
#                 making a list
                List = []
                for j in range(columnsMat_1):
#                     taking elements of matrix from usser
                    elements_1 = int(input("Enter the elements of Matrix 1 ({},{}):".format(i,j)))
                    List.append(elements_1) #append each element in a list
                matrix_1.append(List) #append tha upper list a new matrix from this we will get a nested list
            print("<---------------------------------------------------------------->")
#             same here getting input from user and apending those elements in a new list
            for i in range(rowsMat_2):
                List = []
                for j in range(columnsMat_2):
                    elements_2 = int(input("Enter the elements of Matrix 2 ({},{}):".format(i,j)))
                    List.append(elements_2)                    
                matrix_2.append(List)
            print("<---------------------------------------------------------------->")
            List1 = []
            
            y=0
#             print(matrix_1,"   ",matrix_2)
            while y < len(matrix_1):
                List1= []
                for i in range(len(matrix_1)):  
                    Sum = 0
                    for j in range(len(matrix_1[i])): # getting each value of matrix one
                        Sum+= matrix_1[y][j]*matrix_2[j][i] #multiplying the row of matrix one with column of matrix two     
                    List1.append(Sum) # again appending each value in a new list
                matrix_3.append(List1) #appending the new values in a new matrix
                y+=1
            
            print("""Output Matrix            
            """)
            print("""In Form of List""")
            print(matrix_3) # printing the value  in form of nested list
            print()
            print("Without List Form")
            for i in matrix_3:
                for j in i:
                    print(j,end="  ") #print the through loop
                print()
                    
        else:
            print("Error! column of the first matrix not equal to row of the second second matrix")
            matrixMult()
matrixMult()


    
                        
        


# In[ ]:


### Extra Tasks
# this program checks whether the given value is a perfect number or not
def perfect_number(value):  
#  we will check for the factors of the value
    def factor(num):
        total_sum = 0
        for i in range(1,num):            
            if num % i == 0:
#      sum the total number of factors of the value
                total_sum += i
#     return the sum of factors
        return total_sum
    total_sum = factor(value)
#     check wheter the total_sum is equal to value or not
    def check():
        if total_sum == value:
            print(value,"is a perfect number")
        else:
            print(value,"is not a perfect number")
    check()

number = int(input("enter the number: "))
perfect_number(number)


# In[2]:


# inputs the rows form user
rows = int(input('enter number'))
counter = 0
Counter = rows
for i in range(rows,0,-1):
#     builds one side of Diamond using loops
    for j in range(i):
        print(' ',end="")
    for k in range(i,rows+1):
        print(counter,end='')
    for l in range(i,rows):
         print(counter,end="")
    counter+=1
    print()
for i in range(rows+1):
    for j in range(i):
         print(' ',end="")
    for k in range(rows,i,-1):
         print(Counter,end='')
    for l in range(i,rows+1):
         print(Counter,end="")
    Counter-=1
    print()


# In[23]:



# In[ ]:




