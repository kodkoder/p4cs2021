import json
students= []

def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Save students")
    print("\t(q) Quit")

    choice = input("type one letter (a/v/s/q):").strip()
    return choice

filename="testdict.json"

sample = dict(name='fred', age=31, grades=[1,34,55])
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

def readDict():
     # this will throw an error if the file does not exist
 # it should readly just return an empty dict
 # we can do this later
    with open(filename) as f:
        return json.load(f)


def doAdd(students):
    # you have code here to add
    print("in adding")
def doView(students):
    # you have code here to view
    print("in viewing")
def doSave(students):
#you will put the call to save dict here
    print("in save")
    writeDict(students)
    print("students saved")
def doLoad(students):
    return readDict()

# in the menu
students = doLoad()
#main program

choice = displayMenu()
while(choice != 'q'):
# we could do this with lamda functions
# I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice == 'l':
        doLoad(students)
    elif choice !='q':
        print("\n\nPlease select either a,v,s or q")
    choice=displayMenu()