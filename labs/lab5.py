students = {}
grades = []
con = 'yes'
while con != 'no':
    id = input("please enter student ID:")
    name = input("Please enter student names:")
    students[id] = name
    print(students.items())
    con = input("Do you have more to input, press yes to continue/ no to finish")

number = int(input("how many assignments?"))
print(students)
for id in students:
    for i in range(number):
        #if grades > 0 and grades < 100 :
        grades.append(input("please enter score"+' '))
        print(grades)
        #else:
        #   print("please input again")
    students[id] = (grades) #append()
    print(students)
