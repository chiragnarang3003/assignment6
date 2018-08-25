'''
#Question1:->Create a circle class and initialize it with radius. 
Make two methods getArea and getCircumference inside this class.
'''
class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print("Area of the circle is : ",self.pi*self.radius*self.radius)
        

    def getCircumference(self):
        print("Circumference of a circle is : ",2*self.pi*self.radius)
rad=int(input("Radius of a circle is : "))
cr=circle(rad)
cr.getArea()
cr.getCircumference()
print()

'''
#Question2:->Create a Student class and initialize it with name and roll number. Make methods to : 
1. Display - It should display all informations of the student. 
2. setAge - It should assign age to student 
3. setMarks - It should assign marks to the student. 
'''
class student:
    age=20  #class level variables(static variables)
    marks=75
    def __init__(self,name,rollno):
        self.name=name
        self.roll=rollno
    def setAge(self,age):
        self.age=age
    def setmarks(self):
        return self.marks
    def Display(self):
        print("Name : {} ,roll number : {} ".\
              format(self.name,self.roll),end=' ')
        print("Age : ",self.age)
std1=student('Chirag',1253)
std1.Display()
std2=student('Bandita',1218)
std2.Display()
std3=student('Sakshi',101197)
std3.Display()
print("marks of student sakshi is : ",std3.setmarks())
print()

'''
#Question3:->Create a Temprature class and create two methods: 
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius. 
'''
class Temprature:
    def __init__(self,temp):
        self.temperature=temp
    def convertFahrenheit(self):
        '''take temperature as celsius temperature and convert it into fahrenheit'''
        self.convertF=1.8*self.temperature
        print("Temperature in Fahrenheit is : ",self.convertF)
    def convertCelsius(self):
        '''take temperature as fahrenheit temperature and convert it into celsius'''
        self.convertC=(self.temperature-32)*(5/9)
        print("Temperature in Celsius is : ",self.convertC)
te1=Temprature(35);
te1.convertFahrenheit()
te1.convertCelsius()
print()

'''
#Question4:->Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details.
'''
class MovieDetails:
    def __init__(self,an,yor,rat):
        self.artist_name=an
        self.year_of_release=yor
        self.ratings=rat
    def Display(self):
        print("artist name : {} , year of Release : {} , Ratings : {},".\
              format(self.artist_name,self.year_of_release,self.ratings,end=" "))
        print("Name of the movie is : {} , Type : {} ".\
              format(self.movie_name,self.type))
    def add(self,mn,typ):
        self.movie_name=mn
        self.type=typ
name=input("Enter movie name : ")
artist=input("Enter the name of the artist : ")
release=int(input("Enter year in which movie is released : "))
ratings=int(input("Enter ratings of the movie : "))
type_of_movie=input("Enter type of movie(romentic,action,..) : ")
MD=MovieDetails(artist,release,ratings)
MD.add(name,type_of_movie)
MD.Display()
print()

'''
#Question5:->Create a class Animal as a base class and define method animal_attribute. 
Create another class Tiger which is inheriting Animal and access the base class method.
'''
class Animal:
    def animal_attribute(self):
        print("Class animal is a Base class")
class Tiger(Animal):
    def __init__(self):
        print("Class Tiger is a child class and it inherits the base class Animal")
a1=Animal()
a1.animal_attribute()
a2=Tiger()
a2.animal_attribute()
print()

'''
#Question6:->What will be the output of following code.
'''
'''
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
'''
#Answer:->Invalid syntex


#if we make a little change in print statement...like:---->
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print( a.f(), b.f())
#it will give output (A B).
print()

'''
#Question7:->Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
'''
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        return self.length*self.breadth
class rectangle(Shape):
    def __init__(self,length,breadth):
        super(rectangle,self).__init__(length,breadth)
class square(Shape):
    def __init__(self,length):
        super(square,self).__init__(length,length)
shape1=Shape(4,8)
rect=rectangle(4,6)
square1=square(5)
print("Area of rectangle is : ",rect.Area())
print("Area of square is : ",square1.Area())
print()
        
        


































