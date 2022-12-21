# Your code for Add_Student goes here

# Add_Stuednt
def Add_Student(x,y):
    x.update(y)
    return x
Student1={"p21-2353":["ali","ali",True,3.98,7]}
Add_Student(Student,Student1)

#Your code for Search_Student goes here

# search_ student
def Search_Student(a,b):
    dic={}
    b=b.split(" ")

    for i in a:
        if Student[i][0:2]==b:
            dic[i]=Student[i]
            return dic
        
    return dic

    
b=input("student_name=")    
    
Search_Student(Student,b)


#Your code for Update_Student goes here

# Update_Student
def Update_Student(c,v):
    for i in c:
        if i==v[0]:
            if v[1]=="CGPA":
                c[i][3]=v[2]
            elif v[1]=="First_name":
                c[i][0]=v[2]
            elif v[1]=="Last_name":
                c[i][1]=v[2]
            elif v[1]=="boolen":
                c[i][2]=v[2]
            elif v[1]=="semester":
                c[i][4]=v[2]            
    return c             

x=["p21-2353","CGPA",2.0]    
Update_Student(Student,x)    


#Your code for Delete_Student goes here

# Delete_Student
def Delete_Student(p,q):
    q=q.split(" ")
    for i in p:
        if p[i][0:2]==q:
            del p[i]
            return p
    return p
    
x=input("Delete the Student name")    
    
Delete_Student(Student,x) 
#Your code for Get_Students goes here
# Get_Student
def Get_Student(t):
    CGPA=[]
    Semester=[]
    twice =[]
    for i in t:
        for j in t:
            if t[i]!=t[j]:
                if t[i][3]==t[j][3]:
                    n=t[i][0]+" "+t[i][1]
                    if n not in CGPA:
                        CGPA.append(n)
                if t[i][4]==t[j][4]:
                    x=t[i][0]+" "+t[i][1]
                    if x not in Semester:
                        Semester.append(x)
                if t[i][4]==t[j][4] and  t[i][3]==t[j][3] :
                    y=t[i][0]+" "+t[i][1]
                    if y not in twice:
                        twice.append(y)
        
    total =[]
    total.append(CGPA)
    total.append(Semester)
    total.append(twice)
    return total
    
             
    
    
    
    
Get_Student(Student)

