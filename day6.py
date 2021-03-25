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
