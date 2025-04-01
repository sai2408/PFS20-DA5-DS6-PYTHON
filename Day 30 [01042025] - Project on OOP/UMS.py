class person:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
class student(person):
    def __init__(self,rollno,name,branch):
        super().__init__(rollno,name)
        self.branch = branch
class teacher(person):
    def __init__(self,rollno,name,subject):
        super().__init__(rollno,name)
        self.subject = subject
class college:
    def __init__(self,cname):
        self.cname = cname
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        pass
    def display_teachers(self):
        pass
colleges = []
while True:
    print("Choose the Required option: ")
    print("1. Create College.")
    print("2. Add Student.")
    print("3. Add Teacher.")
    print("4. Display Students.")
    print("5. Display Teachers.")
    print("6. Exit.")
    x = int(input("Enter your Option: "))
    if x == 1:
        clgname = input("Enter College Name: ")
        temp = False
        for x in colleges:
            if clgname == x.cname:
                temp = True
                break
        if temp == True:
            print()
            print("College Already Exists !")
            print()
        else:
            clg = college(clgname)
            colleges.append(clg)
            print()
            print("College Added Sucessfully")
            print()
    elif x == 2:
        clgname = input("Enter College Name: ")
        temp = False
        for x in colleges:
            if clgname == x.cname:
                clg = x
                temp = True
                break
        if temp == True:
            rollno = input("Enter Roll no: ")
            name = input("Enter Student Name: ")
            branch = input("Enter Student Branch: ")
            s1 = student(rollno,name,branch)
            clg.add_student(s1)
            print()
            print("Student Added Sucessfully ")
            print()
        else:
            print()
            print("College Does not Exists !")
            print()
    elif x == 3:
        clgname = input("Enter COllege Name: ")
        temp = False
        for x in colleges:
            if clgname == x.cname:
                clg = x
                temp = True
                break
        if temp == True:
            rollno = input("Enter Rollno: ")
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            t1 = teacher(rollno,name,subject)
            clg.add_teacher(t1)
            print()
            print("Teacher Added Sucessfully !")
            print()
        else:
            print()
            print("College Does not Exists !")
            print()
    elif x == 4:
        clgname = input("Enter COllege Name: ")
        temp = False
        for x in colleges:
            if clgname == x.cname:
                clg = x
                temp = True
                break
        if temp == True:
            details = clg.students
            n = len(details)
            print()
            for i in range(n):
                print(f"Student {i+1}:")
                print(f"Roll Number: {details[i].rollno}")
                print(f"Name : {details[i].name}")
                print(f"Branch: {details[i].branch}")
                print()
        else:
            print()
            print("College Does not Exists !")
            print()
    elif x == 5:
        clgname = input("Enter COllege Name: ")
        temp = False
        for x in colleges:
            if clgname == x.cname:
                clg = x
                temp = True
                break
        if temp == True:
            details = clg.teachers
            n = len(details)
            print()
            for i in range(n):
                print(f"Teacher {i+1}:")
                print(f"Roll Number: {details[i].rollno}")
                print(f"Name : {details[i].name}")
                print(f"Subject: {details[i].subject}")
                print()
        else:
            print()
            print("College Does not Exists !")
    elif x == 6:
        break
    else:
        print()
        print("choose the COrrect Option")
        print()
        






    
