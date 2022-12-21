

def Sum(value):
    sum_items = 0
#     gets all keys and values of the dict
    for i,j in value.items():
        sum_items += j
        print(i,' = ',j)
    #  check whether the sum is even or not  
    if sum_items % 2 == 0:
        print("the sum is even")
    else:
        print("the sum is odd")
#         returns the total sum of values
    return sum_items
thisDict = {
    "one" : 1,
    "two" : 2,
    "three" : 3
    }

sum_items = Sum(thisDict)
     
print("the sum is =",sum_items)
        


# In[ ]:


items = (1,2,3,4,5,5,6,7,8)
product = 1
# gets every element from items
for i in items:
#     multiply every element of items
    product *= i
print("the product of items is:",product)


# In[ ]:





# In[ ]:


def search_element(value,check):
#     get every element in value
    for i in value:
        for j in i:
# checks if the number is present or notmber is present or not and return True or False
            if check == j:        
                return True
    else:
        return False
            
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
element = int(input("enter the element that you want to check: "))
# gives two argument to search_element
Check = search_element(matrix,element)
print(Check)





# In[ ]:


def search_element(value,check):
#     get every element in value
    for i in value:
        if check in i:
#             checks if the number is present or not
            return True
    else:
        return False
            
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
element = int(input("enter the element that you want to check: "))
Check = search_element(matrix,element)
print(Check)


# In[1]:


def gpa_calculator(subject):
    counter = 1
    Sum_total = 0
    Sum_hours = 0
#     taking grade and credict hours from student 
    for i in range(subject):
#         getting values from user
        Sub_grade = input("Please enter your grade in subject ({}): ".format(counter))
        Sub_hours = int(input("Please enter the Credit Hours of Subject ({}): ".format(counter)))
        Sub_grade = Sub_grade.upper()
#         adding grade and credit hours
        Sum_total += (grade[Sub_grade]*Sub_hours)
        Sum_hours += Sub_hours
        counter+=1
#         calculating the total gpa 
    GPA = (Sum_total)/Sum_hours
#     returning the total gpa
    return round(GPA,2)



grade = {
    "A":4.0,
    "A-":3.67,
    "B+":3.33,
    "B":3.0,
    "B-":2.67,
    "C+":2.33,
    "C":2.0,
    "C-":1.67,
    "D+":1.33,
    "D":1.0,
    "F":0
}
# taking input from student that he want gpa for how many subjects
subject = int(input("Enter the number of subjects: "))
GPA = gpa_calculator(subject)
print("Your GPA is: ",GPA)


# In[ ]:





# In[ ]:




