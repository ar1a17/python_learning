"""#how to create function
def my_function():
    a=5
    b=6
    c=a+b
    print(c)
#function calling..
my_function()"""


# one Argument
"""def my_function(fname):
    print(fname+6)

my_function(4)
my_function(6)
"""
# on or more Argument
"""def my_function(fname,lname,vname):
    print(fname + " " + lname + vname)
my_function("ajay","anil","ashutosh")
"""
#arbitrary
"""def my_function(*kids):
    print("the younger child is "+ kids[0])
my_function("ajay","anil","ashutosh")"""
 #keyword Argument
"""def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "ajay", child2 = "anil", child3 = "ashutosh")"""

#class
"""class MyClass:
  x = 5
print(MyClass)"""


#object
"""class MyClass:
  x = 6
p1 = MyClass()
print(p1.x)"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("ajay", 25)
print(p1.name)
print(p1.age)
