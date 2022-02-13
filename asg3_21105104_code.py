################################################################################################################################
###### QUESTION 1 #####
## Taking input from user
n=input("Enter the string - ")
## converting the string to lower case
a= n.lower()
## splitting the string into words
new_list=a.split()
## declaring two empty lists
letter_list=[]
word_list=[]
## Conditioning to distinguish if the entered string is a single word or a sentence... 
if len(new_list)==1:
    ## if the string is a word..
    for i in a:
         ### adding each letter in the letter_list
        letter_list.append(i) 
    ## introducing an empty dictionary    
    di1={}
    ## here letters take place of key and number of their occurences take place of corresponding values in di1
    for j in letter_list:
        if j in di1:
            di1[j]=di1[j]+1
        else:
            di1[j]=1
    print(di1)
        
else:
    ## if the string is not a word..
    for w in new_list:
        ### adding each word in the letter_list
        word_list.append(w)
    ## introducing an empty dictionary  
    di4={}
    ## here words take place of key and number of their occurences take place of corresponding values in di4
    for s in word_list:
        if s in di4:
            di4[s]=di4[s]+1
        else:
            di4[s]=1
            
    print(di4)
################################################################################################################################
###### QUESTION 2 #####
## Taking input date from user...
dd=int(input("Enter current date =  "))
mm=int(input("Enter current month = "))
yyyy=int(input("Enter current year =  "))
## using two different lists which have the numeric value of months....and these are differentiated on basis of number of days..
months_31day=[1,3,5,7,8,10,12]
months_30day=[4,6,9,11]
## conditioning for the given limitiations in the question...
if 1<=dd<=31 and 1<=mm<=12 and 1800<=yyyy<=2025:
    ## specifing for a month with 31 days...
    if mm in months_31day:
        ## for the end case...
        if dd==31:
            ## changing the year...
            if mm==12:
                print("Next Date is:- ",1,"/",1,"/",yyyy+1)
            ## changing the month...
            else: 
                print("Next Date is:- ",1,"/",mm+1,"/",yyyy)
        ## increment in the date by one...    
        else:
            print("Next Date is:- ",dd+1,"/",mm,"/",yyyy)
            
    elif mm in months_30day:
        ## changing the month...
        if dd==30:
            print("Next Date is:- ",1,"/",mm+1,"/",yyyy)
       ## increment in the date by one...         
        else:
            print("Next Date is:- ",dd+1,"/",mm,"/",yyyy)
    ## special case of February...        
    else:
        if mm==2:
            if dd==28:
                ## taking in consideration the case of a leap year...
                if yyyy%4==0:
                    print("Next Date is:- ",29,"/",2,"/",yyyy)
                else:
                    print("Next Date is:- ",1,"/",3,"/",yyyy)
            elif 1<=dd<=27:
                print("Next Date is:- ",dd+1,"/",2,"/",yyyy)
            ## in a leap year
            elif dd==29 and yyyy%4==0:
                print("Next Date is:- ",1,"/",3,"/",yyyy)
            else:
                print("Error...")
                    
else:
    print("Error...")
################################################################################################################################
## QUESTION 3 ###
## Taking the input from user...
li = eval(input("ENTER THE LIST (seperate the entered numbers by commas)  :  "))
## introducing an empty list...
new=[]
## Using loop...
for i in li:
    new.append((i,i**2))
print("The output is - ",new)
################################################################################################################################
##  QUESTION 4 ##
table={}
while True:
    table[10]="Your Grade is ‘A+’ and Performance is Outstanding."
    table[9]="Your Grade is ‘A’ and Performance is Excellent ."
    table[8]="Your Grade is ‘B+’ and Performance is Very Good ."
    table[7]="Your Grade is ‘B’ and Performance is Good ."
    table[6]="Your Grade is ‘C+’ and Performance is Average ."
    table[5]="Your Grade is ‘C’ and Performance is Below Average ."
    table[4]="Your Grade is ‘D’ and Performance is Poor."
    ## Taking the input...
    n=int(input('Enter the Grade Point - '))
    ## Applying the conditioning...
    if 4<=n<=10:
        print(table[n])
        break
    else:
        print("Error...Re-enter the Grade Point.")
################################################################################################################################
### Question 5.  ###
## Taking the input from user....
n=int(input("Enter the integer = "))
## converting A to its ascii value...
x=ord('A')
i=1
while n>=i:
    ## for spaces
    j=1
    while i-1>=j:
        print(' ',end='')
        j=j+1
    ## for characters
    d=1
    while 2*(n-i)-1>=d:
        ## converting ascii value to character...
        charprint=chr(x+d-1) 
        print(charprint,end='')
        d=d+1
    i=i+1
    print()
################################################################################################################################
###  QUESTION 6  ###
## introducing an empty dictionary...
record={}
while True:
    n=input('''Do you want to enter name and SID of student?
              Press Y for Yes and N for No - ''')
    
    
    a=ord(n)
    if a==89:
        Name=input("Enter the name of the student - ")
        SID=int(input("Enter the SID of the student - "))
        
        record[SID]=Name
        

    elif a==78:
        ("Thanks")
        break

print("Printing the record of student information: -  ",record)

print("Sorting on basis of values",sorted(record.values()))
print("Sorting on basis of keys",sorted(record.items()))
p=int(input("Enter the SID to search Name:- "))
if p in record:
    print(Name)
################################################################################################################################
### QUESTION 7 ###
## defining a function for fibonacci numbers
def f(n):  
    if n==2 or n==1:
        return 1
    return f(n-1)+f(n-2)
## taking the input..
n=int(input("Enter the number - "))
print("The required series is - ")
## printing the series...
sum=0
for i in range(1,n+1):
    print(f(i),end=" ")
    sum=sum+f(i)
print("\nTotal sum of the series till the entered term = ",sum)
print("The average is = ",sum)

################################################################################################################################
### QUESTION 8 ###
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
set_4=Set1^Set2
print("a). Set of all elements that are in Set1 and Set2 but not both - ",set_4)
set_5=Set1^Set2^Set3
print("b). Set of all elements that are in only one of the three sets Set1,Set2 and Set3. - ",set_5)
set_6 = (Set1|Set2|Set3) - (Set1^Set2^Set3) - (Set1&Set2&Set3)
print("c). Set of elements that are exactly two of the sets Set1, Set2 and Set3 - ",set_6)
set_7 = set()
for i in range(1,11,1):
    if i not in Set1:
        set_7.add(i)
print("d). Set of all integers in the range 1 to 10 that are not in Set1 - ",set_7)
set9={1,2,3,4,5,6,7,8,9,10}
set_8=set9-(Set1|Set2|Set3)
print("e). Set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3 - ",set_8)
