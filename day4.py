#####class and object#######
"""class Filmstar:
    pass
actor=Filmstar()
actor.name="Ajay"
actor.age=45
actor.films=100
actor.lang=["hindi","english"]
print(actor.lang,actor.films)"""


#__init__ method
"""class Person:

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

najim = Person("najim", 255, "Instructor")
ajay = Person("ajay", 2555, "student")
anil = Person("anil", 14255, "teacher")
ashutosh = Person("ashutosh", 25255, "PT teacher")
print(ajay.name )
"""

"""class MyClass:
  x = 5
  y=5
  z=x+y
p1 = MyClass()#creating object
print(p1.z)"""

"""class gg:
    x=5
    y=4
    z=x>y
a1=gg()
print(a1.z)"""

"""class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("gg", 24)
print(p1.name)
print(p1.age)"""




"""class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name )


p1 = Person("anil", 26)
p1.myfunc()"""
#class method


##inheritance

class Person(object):
    """
    Returns a ```Person``` object with given name.

    """
    def __init__(self, name):
        self.name = name

    def get_details(self):
        "Returns a string containing name of the person"
        return self.name


class Student(Person):
    """
    Returns a ```Student``` object, takes 3 arguments, name, branch, year.

    """
    def __init__(self, name, branch, year):
        super().__init__(name)
        self.branch = branch
        self.year = year

    def get_details(self):
        "Returns a string containing student's details."
        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


class Teacher(Person):
    """
    Returns a ```Teacher``` object, takes a list of strings (list of papers) as
    argument.
    """
    def __init__(self, name, papers):
        super().__init__(name)
        self.papers = papers

    def get_details(self):
        return "%s teaches %s" % (self.name, ','.join(self.papers))


person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
