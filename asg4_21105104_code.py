           #############################################################  ASSIGNMENT 4  ##########################################################################

def tower_hanoi(n,a,b,c):
    if n==1:
        print("Shift 1st disc from",a,"to",c,"\n")
        return
    tower_hanoi(n-1,a,c,b)
    print("Shift disc",n,"from",a,"to",c,"\n")
    tower_hanoi(n-1,b,a,c)
    return
print("QUESTION - 1")
n=int(input("Enter the number of dics = "))
a=input("Enter the name of source = ")
b=input("Enter the name of helper = ")
c=input("Enter the name of destination = ")
tower_hanoi(n,a,b,c)
print("_________________________________________________________________________________________________________________________")


def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print("QUESTION - 2")
n=int(input("Enter the number of rows = "))
for i in range(n):
    for j in range(1,((2*n+1)//2)-i):                ##### or (n+1-i)
        print(end=" ")
    for t in range(i+1):
        print((fact(i)//(fact(i-t)*fact(t))),end=" ")
    print()
print("_________________________________________________________________________________________________________________________")

print("QUESTION - 3")
n=int(input("Enter the Dividend = "))
m=int(input("Enter the Divisor = "))
a,b=divmod(n,m)
print("The Quotient is- {} and The Remainder is - {} ".format(a,b))
g=callable(divmod)
print("a). Is the function - divmod callable?     - Ans.",g)
if a!=0 and b!=0:
    print("b). All the values are non zeros or not?   -Ans.",True)
else:
    print("b). All the values are non zeros or not?   -Ans.",False)
li=[]
li.append(a)
li.append(b)
for i in (4,5,6):
    li.append(i)

for j in li[0:]:
    if j>4:
        pass
    else:
        li.remove(j)
print("c). The database - ",li)
set1=set(li)
print("d). The required database is - ",set1)
set_frozen= frozenset(set1)
print("e). The required immutable set is - ",set_frozen)
d=max(set_frozen)
print("f). The maximum value in the set is - ",d,"and its hash value is - ",hash(d))
print("_________________________________________________________________________________________________________________________")



print("QUESTION - 4")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object is destroyed")

student13 = Student("Vidit Sarin", 21105104)
print("Object is created")
print(f"Student's name is {student13.name} and his/her SID is {student13.sid}.")
del student13
print("_________________________________________________________________________________________________________________________")


print("QUESTION - 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

# creating records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# a).
employee1.salary = 70000
print(f"a). The updated salary of the employee {employee1.name} is {employee1.salary}")

# b).
print("b). ", end='')
del employee3
print("_________________________________________________________________________________________________________________________")



print("QUESTION - 6")
def ana(in1,in2):
    list1=[]
    list2=[]
    sum1=0
    sum2=0
    
    for i in in1:
        list1.append(i)
        sum1+=ord(i)
    for z in in2:
        list2.append(z)
        sum2+=ord(z)
    list1.sort()
    list2.sort()
    if list1==list2  and  sum1==sum2:
         print("STRONG FRIENDSHIP")
    else:
        print("FAKE FRIENDSHIP")
        
    
    
in1=input("Enter the first word here -  ")
in2=input("Enter the second word here -  ")
ana(in1,in2)
print("_________________________________________________________________________________________________________________________")

