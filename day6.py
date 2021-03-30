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
# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n
def largest(arr,n):

	# Initialize maximum element
	max = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max

# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)

# This code is contributed by Smitha Dinesh Semwal
