#Method - 1
'''
x = open("hello1.txt","r")
x.close()
'''
#Method - 2
'''
x = open("hello1.txt","r")
data = x.read()
print(data)
x.close()
'''
#Method - 3
'''
x = open("hello1.txt","r")
data = x.readlines()
print(data)
x.close()
'''
#Method - 4
'''
x = open("hello1.txt","r")
data = x.read()
for i in data:
    print(i)
x.close()
'''
#Method - 5
'''
x = open("hello1.txt","r")
data = x.read(10)
print(data)
x.close()
'''
#Method - 6
'''
a = open("hello2.txt","w")
a.write("Hello Codegnan")
a.close()
'''
#Method - 7
'''
a = open("hello4.txt","w")
a.write("Hello 1\n")
a.write("Hello 2")
a.close()
'''
#Method - 8
'''
f1 = open("hello5.txt","a")
f1.write("Data 1")
f1.close()
'''
#Method - 9
'''
f2 = open("hello5.txt","a")
f2.write("New Data")
f2.close()
'''
#MEthod - 10
'''
f1 = open("hello6.txt","w")
f1.write("Data 1")
f1.close()
'''
'''
f1 = open("hello6.txt","w")
f1.write("Data 2")
f1.close()
'''
#MEthod - 11
'''
f1 = open("hello7.txt","a")
f1.write("Data 1")
f1.close()
'''
'''
f1 = open("hello7.txt","a")
f1.write("Data 2")
f1.close()
'''
'''
f1 = open("hello7.txt","a")
f1.write("\nData 3")
f1.close()
'''
#Method - 12
'''
f3 = open("hello8.txt","r+")
f3.write("Hello Code")
data = f3.read()
print(data)
f3.close()
'''
#MEthod - 13
'''
f3 = open("hello8.txt","a+")
f3.write("Java")
data = f3.read()
print(data)
f3.close()
'''
#MEthod - 14
'''
f3 = open("hello10.txt","a+")
f3.write(" Python")
f3.seek(0)
data = f3.read()
print(data)
f3.close()
'''

































