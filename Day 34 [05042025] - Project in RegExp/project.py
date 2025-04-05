import re
#Name
x = True
while x:
    pattern = re.compile(r'^[A-Za-z ]+$')
    text = input("Enter Your Name: ")
    res = pattern.fullmatch(text)
    if res != None:
        name = res.group()
        break
    else:
        print("Enter Name in Correct Format !")
#Date of Birth
while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    text = input("Enter Date of Birth: ")
    res = pattern.fullmatch(text)
    if res != None:
        dob = res.group()
        break
    else:
        print("Enter DOB in Correct Format !")
#Email id
while True:
    pattern = re.compile(r'[a-z0-9]+@gmail.com\Z')
    text = input("Enter Email id: ")
    res = pattern.fullmatch(text)
    if res != None:
        mailid = res.group()
        break
    else:
        print("Enter Mail id in correct format !")
#Mobile Number
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    text = input("Enter Mobile Number: ")
    res = pattern.fullmatch(text)
    if res != None:
        mobile = res.group()
        break
    else:
        print("Enter Mobile Number in correct Format !")
print(f"Name : {name}")
print(f"Date of Birth: {dob}")
print(f"Mail id: {mailid}")
print(f"Mobile : {mobile}")






    
