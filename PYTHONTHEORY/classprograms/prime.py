#python script to process 3 student details,roll no.,3 subject marks,calculate avg,percentage and display grade based on percentage
#60-75 grade is firstclass,above 75 is distinction  
def rollno(): 
     return int(input("Enter Student Roll number:"))
def Marks():
    total = 0
    for num in range(1,6):
        marks = float(input(f"Enter Subject {num} marks:"))
        total = total + marks
    return total
def Average(total):
    average = total / 5.0
    return average
def Percentage(total):
   percentage = (total*100)/500
   return percentage
def Grade(percentage):
   if percentage < 60:
       Grade = 'Second Class'
   if 60 <= percentage <= 75:
       Grade = 'First Class'
   if percentage > 75:
       Grade = 'Distinction'
   if percentage < 45:
       Grade = 'Failed'
   print(f"Grade scored:{Grade}")
i = int(input("Enter number of students:"))
j = 1
for j in range(1,i+1):
    print(f"For Student {j}:")
    Rollno = rollno()
    total = Marks()
    average = Average(total)
    percentage = Percentage(total)
    print("-----Student Details-----")
    print(f"Roll number:{Rollno}")
    print(f"Total marks:{total}")
    print(f"Average marks:{average}")
    print(f"Percentage:{percentage}")
    Grade(percentage)
    print("--------------------")