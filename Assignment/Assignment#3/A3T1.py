# Your code for dectionary initialization and printing goes here
student = {
    '21p-8027':['Sheryar','sher',True,3.5,1],
    '21p-8028':["Faizan","Ahmad",True,3.1,1],
    '21p-8033':["Abrar",'ulhaq',True,3.3,1],
    '21p-8023':['Asif','Ali',True,3.12,3],
    '21p-8022':['Sajid','Ali',True,3.6,1],
    '21p-8021':['Ayyan',"shabbir",True,3.4,1],
    '20p-8030':["Umais",'ullah',True,3,3],
    '18p-2000':['Saeed','murtaza',True,3.5,7],
    '19p-8032':['Shah','nawaz',False,3.2,4],
    '20p-8012':['Ahtisham','rauf',False,3.12,3]
}
# first method
for rollNo,data in student.items():
    print(rollNo,":",data)
# second method
for rollNo in student:
    print(rollNo,":",student[rollNo])
    
