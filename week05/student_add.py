def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit:").strip()
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"])) 

def doView(students):
     for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);

#test the function
choice = displayMenu()
print("you chose {}".format(choice))

def doView(students):
    # later
    print(students)

#main program
students = []
while(choice != 'q'):
    # we could use lambda
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print('\n\nPlease select one of the options...')
    choice=displayMenu()




