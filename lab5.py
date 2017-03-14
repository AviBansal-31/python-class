students = {}
con = 'yes'
while con != 'no':
    id = input("please enter student ID:")
    name = input("Please enter student names:")
    students[id] = name
    print(students.items())
    con = input("Do you have more to input, press yes to continue/ no to finish")

number = input("how many assignments?")
#        studnets[id][name].append()
