#  Assignment- 2 #

## 1. For a given input string “Python is a case sensitive language”. Write python
##    code for the following:

string="Python is a case sensitive language"

# a. Find the length of the input string.

length=len(string)
print("The length of string is %d"%(length))
        
# b. Reverse the order of the string in one line code.

reversed_string=string [::-1]
print(reversed_string)
        
# c. Using Slice function store “a case sensitive” in new string.
   
new_str=string[slice(10,35,1)]
print("New sliced string:- ",new_str)

# d. Replace “a case sensitive” with “object oriented”.

replaced_string= string.replace("a case sensitive" ,"object oriented")
print("New string:- ",replaced_string)
        
# e. Find index of substring “a” in the given input string.

req_index=string.index("a")
print("Index of required substring is- ",req_index)

#   f. Remove the white spaces from the given input string.

without_spaces_string= string.replace(" " ,"")
print("New string:- ",without_spaces_string)

#___________________________________________________________________________#

## 2. Store your name, SID, department name and CGPA into different variables.
##    With the help of String formatting print the following output:
##    Hey, ABC Here!
##    My SID is 2110XXXX
##    I am from XYZ department and my CGPA is 9.9

## Extra hint:-‘%s’ is used to inject strings similarly ‘%d’ for integers, ‘%f’ for floating-point values, ‘%b’ for binary format. 

name=input('Enter your name here:- ')
SID=int(input("Enter your SID here:- "))
Dep_name=input('Enter your Department Name here:- ')
CGPA=float(input("Enter your CGPA here:- "))

print("Hey, %s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %f"%(Dep_name,CGPA))

#___________________________________________________________________________#

## 3. For a=56 and b=10 with the help of bitwise operators calculate the following:
a=56
b=10
# a. a&b

print("a&b= ",a&b)

# b. a|b

print("a/b= ",a/b)

# c. a^b

print("a^b= ",a^b)

# d. Left shift both a and b with 2 bits.

print("After left shift by 2-bits a= ",a<<2)
print("After left shift by 2-bits b= ",b<<2)

# e. Right shift a with 2 bits and b with 4 bits.

print("After right shift by 2-bits a= ",a>>2)
print("After right shift by 2-bits b= ",b>>4)

#____________________________________________________________________________#

## 4. Write a python program to find the greatest of three numbers entered by the user.

# Taking input from user...

num1=int(input("Enter the first number-  "))
num2=int(input("Enter the second number-  "))
num3=int(input("Enter the thied number-  "))

if num1>=num2 and num1>=num3:
    print("The greatest number is-",num1)
    
elif num2>=num1 and num2>=num3:
    print("The greatest number is-",num2)
else:
    print("The greatest number is-",num3)

#____________________________________________________________________________#

## 5. Write a python program to check if the word “name” is present in the string entered by the user (Print : “Yes” or “No”).

# Taking input from user...

user_input=input("Enter the sentence/string - ")
string1="name"
if string1 in user_input:
    print("Yes")
else: 
    print("No")

#____________________________________________________________________________#

## 6. For any three lengths, there is a simple test to see if it is possible to form a
##    triangle. If any of the three lengths is greater than the sum of the other two,
##    then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
##    converts them to integers, and to check whether the given input lengths can
##    form a triangle or not (Print : “Yes” or “No”).

# Taking input from user...

num1=float(input("Enter the first side-  "))
num2=float(input("Enter the second side-  "))
num3=float(input("Enter the thied side-  "))

if num1>num3+num2 or num2>num2+num3 or num3>num1+num2:
    print("No..the given input lengths cannot form a triangle")

    
else:
    print("Yes..the given input lengths can form a triangle")


