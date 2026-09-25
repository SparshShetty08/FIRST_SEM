# python script to process student details, roll no., 5 subject marks,
# calculate average, percentage and display grade based on percentage
# 60-75 grade is First Class, above 75 is Distinction

def rollno():
    return int(input("Enter Student Roll number:"))


def Marks():
    total = 0
    for num in range(1, 6):
        marks = float(input(f"Enter Subject {num} marks:"))
        total = total + marks
    print(f"Total marks:{total}")
    return total


def Average(total):
    average = total / 5.0
    print(f"Average marks:{average}")
    return average


def Percentage(total):
    percentage = (total * 100) / 500
    print(f"{percentage}%")
    return percentage


def Grade(percentage):
    if percentage < 45:
        Grade = 'Failed'
    elif percentage < 60:
        Grade = 'Second Class'
    elif percentage <= 75:
        Grade = 'First Class'
    else:
        Grade = 'Distinction'
    print(f"Grade scored:{Grade}")
    return Grade


i = int(input("Enter number of students:"))

for j in range(1, i + 1):
    print(f"For Student {j}:")
    rollno()
    total = Marks()
    Average(total)
    Percentage(total)
    Grade(Percentage(total))
    print("--------------------")