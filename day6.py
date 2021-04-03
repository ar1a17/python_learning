"""class Person: # parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person): # child class
  def __init__(self, fname, lname):
    super().__init__(fname, lname) #using super class
    self.graduationyear=2020 # additional option
    self.fathername="vs rawat" # additional option
x = Student("ajay", "rawat")
print("my name is "+x.firstname, x.lastname,"and my fathername is "+x. fathername,"and my graduationyear is ", +x.graduationyear)

"""




"""import mymod as mx

a = mx.person1["country"]
print(a)
"""
"""
import platform

x = platform.system()
print(x)"""

"""import mydata
a=mydata.add(5,6)
print(a)"""
#exercise
"""def swaplist(list):
    L=list[-1],list[0]
    list[0],list[-1]=L
    return list
newlist=[12,25,26,23]
print(swaplist(newlist))
"""
#exercise 2
"""def swaplist(list):
    start,*middle,end= list
    list =[end,*middle,start]
    return list
newlist=[12,52,8]
print(swaplist(newlist))"""

#exercise 3
"""def swapList(list):

    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list
newlist=[12,5,4,8,9]
print(swapList(newlist))"""

#exercise 4
"""arr=[]
arr=[12,5,4]
ans=sum(arr)
print("sum of the array",ans)
"""

#exercise 4
"""
def largest(arr,n):


	max = arr[0]


	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)"""




"""def sumOfSeries(n):
    x = (n * (n + 1)  / 2)
    return (int)(x * x)

n = 5
print(sumOfSeries(n)"""


"""

import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")
#make cursor
cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT
      (ADMISSION INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      COURSE        CHAR(50),
      DEPARTMENT        CHAR(50));''')
print("Table created successfully")

con.commit()
con.close()

"""


"""
import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()

cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')");

con.commit()
print("Record inserted successfully")
con.close()
"""
"""
#retriving data
import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")


cur = con.cursor()
cur.execute("SELECT admission, name, age, course, department from STUDENT")
rows = cur.fetchall()

for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

print("Operation done successfully")
con.close()
"""
