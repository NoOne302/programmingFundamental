#-------------------- Your code for Add_Student goes here-----------------


def Add_Student(student,newStudent):
    student.update(newStudent)
    return student

stu={'19p-8512':['kashan','ilyas',False,3.2,5]}
student = Add_Student(student,stu)
print(student)


#----------------------- Your code for Search_Student goes here---------------

def Search_Student(student,name):
#     making a new dict to store the new values of our require data
    studentInfo = {}
    for rollNo in student:
#         checking if the name is present or not in student dict
        if name == student[rollNo][0:2]:
            studentInfo[rollNo] = student[rollNo]
#             if name if present them it will store overall data of that student in new dict and return it
            return studentInfo
        
    else:
#         if name is not present them this will return an empty dict
        return studentInfo
# take the name from user and them split the name of user because we have store  first and last name sparetly
name = input("enter the name of student: ")
name = name.split(' ')
studentInfo = Search_Student(student,name)
print(studentInfo)



#-------------- Your code for Update_Student goes here-------------


def Update_Student(student,data):
#     cheking in student if the given rollNo is present or not
    for rollNo in student:
#         if rollNo is present then just updating with given data
        if rollNo == data[0]:  
            if data[1] == "First_name":
                student[rollNo][0] = data[2]
            elif data[1] == "Last_name":    
                student[rollNo][1] = data[2]
            elif data[1] == "is_Registered Student":
                student[rollNo][2] = data[2]
            elif data[1] == "CGPA":
                student[rollNo][3] = data[2]
            elif data[1] == "Semester":
                student[rollNo][4] = data[2]
            return student
    else:
        return "roll number not found"
    
                
            
        
student = Update_Student(student,["21p-807","CGPA",4])
print(student)



# ---------------------Your code for Delete_Student goes here----------

def Delete_Student(student,name):
    for rollNo in student:
#         checking if the given name is equal to any name in student
        if name == student[rollNo][0:2]:#this is to check because fName and lName is at index(0 and 1)          
            del student[rollNo]
            return student
    else:
        return "Name not found"
name = "Sheryar sher"
# spliting name to check in list index(o:2)
name = name.split(' ')
newStudents = Delete_Student(student,name)



#---------- ----Your code for Get_Students goes here------------

def Get_Student(student):
#     creating empty list that we will use in this program
    commonStudents = []
    CGPA = []
    semister = []
    both = []
#     running a lopp to get rollnumber of every student from dict
# here rollNo is for to get a particular roll number 
    for rollNo in student:
#         now runing a loop to in roll number to get detail of that particular rollNum
# here RollNum is to compare the previous student(rollNO) with every student(RollNo)
        for RollNum in student:
##     and checking that if the CPGA if any student is same to any other or not         
            if student[rollNo] != student[RollNum]:#this is to prevent(outer student != to inner loop student)
                if student[rollNo][3] == student[RollNum][3]:
                    fullName = student[rollNo][0] + student[rollNo][1]
#                     if any student have same cgpa to other then appending his name in new list(CGPA)
                    CGPA.append(fullName)
#     here cheking for same semister and doing the same thing if semister is same to anyother than appending in list(Semister )
                if student[rollNo][4] == student[RollNum][4]:
                    fullName = student[rollNo][0] + student[rollNo][1]
                    if fullName not in semister:
                        semister.append(fullName)
#             // here checking if the students have both same semister and CGPA
                if student[rollNo][3] == student[RollNum][3] and student[rollNo][4] == student[RollNum][4]:
                    fullName = student[rollNo][0] + student[rollNo][1]
                    both.append(fullName)
#     appending all list into on main list(commonStudents)                    
    commonStudents.append(CGPA)                    
    commonStudents.append(semister)
    commonStudents.append(both)
        
    return commonStudents
commonStudents = Get_Student(student)
print(commonStudents)

