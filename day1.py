#a=10+52
#print(a)

#a=10<55
#print(a)
#name="ajay"
#print(name)

#how to get user input
#number=int(input("enter the digit:"))
#if number<100:
#     print("your number smaller than 100")
#else:
#     print("your number greater than 100")
#a ,v    = 5 , 6
#print(v)

#data=("ajay",25,"male")
#name,age,sex=data
#print(age)
# Formatting strings
#marks=45
#marks=56
#print(f"the marks is {marks}")

#name= "ajay"
#age=25
#print(f"the is name {name} and the age is {age}")


#.Formatting
#name="ajay"
#age=25
#user="{0}{1}" .format(name,age)
#print(user)

#integer arithmetic
#days=int(input("enter the days:"))
#months = days/30
#days = days % 30
#print("months = %d days = %d" % (months,days))

# 2 method easy way to use interger arithmetic
#days=int(input("Enter the days :"))
#print("months=%d,days=%d"%(divmod(days,30)))

#Relational Operator
#"a=2.5
#"str(a)
#print(a)

#if else statement
#x=int(input("enter the value: "))
#if x>0:
#    x=0
#    print('negitive change the zero')
#elif x==0:
#    print("zero")
#elif x==1:
#    print('single')
#else:
#    print('more')
#while loop
#x=0
#while x<11:
#    print(x)
#    x+=1
#a,b=0,1
#while b<100:
#    print(b)
#    a,b=b, a+b
#multiplication table
"""i = 1
print("-" * 50)
while i < 11:
    n = 1
    while n <= 12:
        print("%4d" % (i * n), end=' ')
        n += 1
    print()
    i += 1
print("-" * 50)"""

#printing star
#row=int(input("enter the number of row:"))
#n=row
#while n>=1:
#    x="*" * n
#    print(x)
#    n-=1
#list
"""a=[1,2,'ajay','india']
print(a[1:2])
"""
"""str="hello this is ajay"
print(len(str))
print(str[0:7])"""
#for loop
"""for i in range(0,10):
    print(i)
else:
    print("bye")"""
"""a=['ajay','ashutosh']
for c in a:
    print(c)"""
#append
"""a=[2,65,6,4]
a.append(45)
print(a)
"""
"""data={'ajay':'','ashutosh','anil'}
print(data)"""

from mydata import person1

print (person1["country"])
