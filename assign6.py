'''
#Question1:->Create a function to calculate the area of a sphere by taking radius from user.
'''
def area_sphere(num):
    '''Calculate the area of the sphere using Fuctions'''
    pi=3.14
    temp=4*pi*num*num
    return temp
radius=int(input("Enter radius of the sphere : "))
output=area_sphere(radius)
print("The area of the sphere is :",output)
print()

'''
#Question2:->Write a function “perfect()” that determines if parameter number is a perfect number.
 Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
 sum to the number. E.g., 6 is a perfect number because 6=1+2+3]. 
'''
def perfect(num):
    '''Print all the perfect numbers lies in range (1,1000) '''
    result=0
    temp=num
    for i in range(1,num):
        if (num%i==0):
            result=result+i
    if (result==temp):
        print(temp)
for i in range(1,1001):
    perfect(i)
print()

'''
#Question3:->Print multiplication table of n using loops, where n is an
integer and is taken as input from the user.
'''
def table(num):
    '''Multiplication table of nth table'''
    for i in range (1,11):
        temp=num*i
        print(num,'*',i,"=",temp)
num1=int(input("Enter the table value you want to see the table : "))
table(num1)
print()

'''
#Question4:->Write a function to calculate power of a number
raised to other ( a^b ) using recursion.
'''
def power(a,b):
    '''Power of a number....(the output comes in return is of float value)'''
    num2=a
    if b==0:
        return a/a
    else:
        return(a*power(a,b-1))  
value=int(input("Enter a number : "))
power1=int(input("Enter power of a number : "))
print(power(value,power1))

#or(Method 2)
def power(a,b):
    '''Power of a number....(the output comes in return is of integer value)'''
    num2=a
    if b==1:
        return a
    else:
        return(a*power(a,b-1))  
value=int(input("Enter a number : "))
power1=int(input("Enter power of a number : "))
print(power(value,power1))
print()

#CLASSES AND OBJECTS:-->
'''
#Question1:->Get keys corresponding to a value in user defined dictionary.
'''
dict1=eval(input("Enter a dictionary : "))
val=(input("Enter a key whose value you want to print : "))
for key,value in dict1.items():
    if (value==val):
        break;
print(key)
print()

'''
#Question2:->Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that ductionary for every subject.
'''
student={'Chirag':{'maths':50,'physics':60,'chem':90},'Bandita':{'maths':90,'physics':95,'chem':99},'Sakshi':{'maths':100,'physics':99,'chem':100},'Hursh':{'maths':85,'physics':30,'chem':90}}
k1=input("enter the name of student whose marks you want to see:")
for key,value in student.items():
    if k1 == key:
        print(value)
print()     













