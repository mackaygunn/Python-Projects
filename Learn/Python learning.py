#_______________________________________________built in functions and modules______________________

#______________built in functions____________________
#dir(__builtins__)
#help() #to get to know about the functions and modules (add needed to knwo inside the brackets)

#______________modules_______________
#[import ....... (math, datetime)
#math. .....] (functions inside the module)


#______________user defined functions:___________________
#def sum(num1, num2): #num1 and num2 are parameters/arguements
 #   return num1 + num2

#print(sum(10, 20))



#_________________________________________________data types____________________________________
#______________lists____________________
#list_1 = [parameters, parameters] #square brackets are used to define a list
#list_2 = list(parameters, parameters) #list function
                                                                                                              #mutable list
#my_list = ['kamal', 20, 'kandy', False, 20, [4, 5, 6]] #accessing data from random places in the list

#print(my_list[1:3]) #slicing the list
#print(my_list[5][0])

#my_list[2] = 'Colombo' #changing the value of the list
#print(my_list)

#_________________tuples____________________
#tuple = (23, 54, 65, 76) #immutable list
#print(tuple[1:3]) #slicing the tuple

#tple = list(tuple) #changing the tuple to a list
#print(type(tple)) 

#__________________sets____________________
#my_set = {'kamal', 20, 'kandy', False, 20}  #set does not allow duplicates and it is unordered and cant be indexed
#print(my_set) 

#A = {1, 2, 3, 4, 5, 6, 7}
#B = {8, 9, 10, 11}

#print(A.union(B)) #combining two sets
#print(A.intersection(B)) #getting the common values in two sets
#print(A.difference(B)) #getting the values in A that are not in B
#print(A.issubset(B)) #checking if A is a subset of B
#print(A.issuperset(B)) #checking if A is a superset of B



#__________________dictionaries____________________
#my_dict = {'name': 'kamal', 'age': 20, 'city': 'kandy'} #key: value pairs
#print(my_dict['name']) #accessing the value of a key in the dictionary
#my_dict['name'] = 'nimal' #changing the value of a key in the dictionary
#rint(my_dict)
#my_dict['country'] = 'sri lanka' #adding a new key value pair to the dictionary
#print(my_dict)
#my_dict.update({'name': 'Sunil'}) #updating the value of a key in the dictionary
#print(my_dict)
#print(my_dict.pop('name', "not found")) #removing a key value pair from the dictionary and returning the value of the key
#print(my_dict)


#____________________________________________break and continue statements____________________
#continue #skip the loop
#break #stops the loop


#def student(subject, marks, **friends):
 #   for key, value in friends.items():
  #      print(key, "=", value)

#student("ramiru", 59, kamal=69, saman=50)



#____________________________________________________________arguements and definitions_____________________________________________________

#def student_info(name, age=15):
#    print(f"My name is {name}. My age is {age}")

#student_info("kamal", 20)



#def total_marks(*marks):
#    total = 0
#    for mark in marks:
#        total += mark
#    print(total)

#total_marks(87, 91, 15)



#def total_marks(**kwargs):
 #   for sub, mark in kwargs.items():
  #    print(sub, mark)

#total_marks(Maths=87, science=50, english=99)

#___________________________________________________OBJECTS AND CLASSES___________________________________
#class phone:
#    def say(self, name):
#        self.x = name
#        print("hello " + name)

#phone1 = phone()
#phone1.say("nokia")
##print(phone1.x)
#phone1.x = "apple"
#print(phone1.x)

#phone2 = phone()
#phone2.say("samsung")


#class student:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
  
#std1 = student("Kamal", 23)
#std2 = student("Nimal", 43)

#print(std1.name, std1.age)
#print(std2.name, std2.age)

#__________private variables and methods___________________________________________
#class myclass:
 #   x = 10             #to make a variable private add "__" before the required variable
  #  __y = 20;
   # def disp(self):
    #    return self.__y

#myobj = myclass()
#print(myobj.disp())



#class myclass:
#    def meth1(self):              #to make a method private add "__" before the required methd and introduce in the first method
#        print("Hello")
#        self.__meth2()

 #   def __meth2(self):
 #       print("Welcome")


#myobj = myclass()
#myobj.meth1()

#__________inheritance___________________________________________
#class phone1:
#    def feature1(self):
#        print("Camera")

#class phone2:
#    def feature2(self):
#        print("internet")

#class phone3(phone2, phone1):
 #   def feature3(self):
  #      print("Bluetooth")

#myobj = phone3()
#myobj.feature1()


#class phone1:
 #   def feature1(self):
  #      print("Camera")

#class phone2(phone1):
 #   def feature2(self):
  #      print("internet")

#class phone3(phone2):
 #   def feature3(self):
  #      print("Bluetooth")

#myobj = phone3()
#myobj.feature3()

#class parent():
 #   def func1(self):
  #      print("Hello")

#class child(parent):
 #     super().func1()
   #     print("welcome")

#myobj = child()
#myobj.func2()





#class parent():
 #   def func1(self):
  #      print("Hello")

#class child(parent):
 #   def func2(self):
  #      print("welcome")
    #def func1(self):
   #     print("hi")

#myobj = child()
#myobj.func1()


#class fruit():
 #   number_of_fruits = None
  #  unit_price = None

   # def set_value(self, x, y):
    #    self.number_of_fruits = x
     #   self.unit_price = y

#class apple(fruit):
 #   def price(self):
  #      print("For apple ", self.number_of_fruits * self.unit_price)

#class orange(fruit):
 #   def price(self):
  #      print("for orange ", self.number_of_fruits * self.unit_price)

#class grapes(fruit):
 #   def price(self):
  #      print("for grapes ", self.number_of_fruits * self.unit_price)

#myobj1 = apple()
#myobj2 = orange()
#myobj3 = grapes()

#myobj1.set_value(23, 45)
#myobj2.set_value(56, 78)
#myobj3.set_value(98, 65)

#myobj1.price()
#myobj2.price()
#myobj3.price()

#______________________________________________datetime module___________________________________________

#__________________date________________________________________________
#import datetime

#b_day = datetime.date(2005, 4, 2)
#print(b_day)

#today = datetime.date.today()
#print(today)

#print(b_day.strftime('%A, %B %d, %Y'))

##age = today - b_day
#print(age)

#print(today.weekday())
#print(today.isoweekday())

#__________________time________________________________________________
#import datetime

#t = datetime.time(9, 30, 45, 10000)
#print(t)
#print(t.hour)

##x = datetime.datetime.today()
#print(x)
#print(x.date())
#print(x.time())

#t_delta = datetime.timedelta(days = 20)
#print(x-t_delta)

#______________________________________________turtle module___________________________________________

#import turtle

#x = turtle.Turtle()

#x.forward(100) #arguement is the distance
#x.turn(90) #arguement is the angle
#x.shape('turtle')
#x.color('red')

#______________________________________________factorial___________________________________________

#result = 1

#for i in range(1, 5):
#    result = result * i

#print(result)  

#x = int(input("enter number "))

#result = 1

#for i in range(1, x+1):
#    result = result * i

#print(result)

#______________________________________________factorial using recursion___________________________________________

#def fact(n):
#    if n == 0:
 #       return 1
 #   else:
  #      return n * fact(n-1)


#print(fact(0))


#______________________________________________lambda function___________________________________________

#area = lambda x: x*x
#print(area(5))

#area = lambda z, y: z*y
#print(area(4, 5))

#def apple(unit_price):
 #   return (lambda number_of_apples: number_of_apples*unit_price)

#x = apple(8)
#print(x(5))

#______________________________________________filter,map, reduce functions___________________________________________

#_________________________filter________________
#number = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

#def even_number(x):
 #   return x % 2 == 0

#print(list(filter(even_number, number)))

                                                          #to filter from a list


#nnumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(list(filter(lambda x: x % 2 == 0, nnumber))) #using lambda function


#_________________________map_______________

#number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#def squareed(x):
 #   return x * 2 

#print(list(map(squareed, number)))                       #to apply operation to each element in a list


#print(list(map(lambda x: x * 2, number ))) #using lambda function


#_________________________reduce_______________
#from functools import reduce

#number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                                              #Used to add all elements in a list together
#def sum(x, y):
 #   return x + y

#print(reduce(sum, number))

#______________________________________________decorators___________________________________________
#def new(func):
 #   def inside(a,b):
  #      if b==0:
   #         a,b = b,a
    #    return func(a,b)
    #return inside

#def divide(a,b):
 #   return a/b

#divide = new(divide)

#print(divide(5,0))

#______________________________________________exception handling___________________________________________
#try:
 #   a = int(input("enter first number "))
  #  b = int(input("enter second number "))
   # print(a/b)
#except:
 #   print("something went wrong ")
  #  print("bye")


#try:
 #   a = int(input("enter first number "))
  #  b = int(input("enter second number "))
   # print(a/b)

#except Exception as e:
 #   print("something went wrong ", e)

#finally:
 #   print("bye")



#try:
 #   a = int(input("enter first number "))
  #  b = int(input("enter second number "))
   # print(a/b)

#except ZeroDivisionError as e:
 #   print("Cant divde by zero", e)

#except ValueError as e:
 #   print("use integers", e)

#except Exception as e:
 #   print("something went wrong ", e)

#finally:
 #   print("bye")

#______________________________________________array___________________________________________
#import array
#x = array.array('i', [2, -3, 7, 8, 9])
#print(x)
#print(x)
#print(x[1:4]) #print from one end to another


#from array import *
#x = array('i', [7,8,9])
#y = array('i', [2, -3, 4, 5, 6])
#print(y)
#y.append(int(input("enter number ")))
#print(y)
#y.extend([7,8,9]) #add multiple values at the same time
#print(y)
#y.insert(2, 6) #add values to required index
#print(y)
#y.pop() #remove element from the end
#y.pop(0) #remove element from needed index
#print(y)
#y.remove(-3) #remove element by element

#z = x+y
#print(z)

#for i in range(len(z)):
 #   print(z[i])

#for i in z:
 # print(i)

#______________________________________________iterators___________________________________________
#list = {3, 5, 7}

#itr = iter(list)
#print(itr)
#print(next(itr))
#print(next(itr))
#print(next(itr))

#while True:
 #   try:
  #    print(next(itr))
   # except StopIteration:
    #  break


#______________create our own iterator___________________________________________
#class myit:
 #   def __init__(self):
  #      self.y=2
   # def __iter__(self):
    #    return self
    #def __next__(self):
     #   val = self.y
      #  self.y+=2
       # return val
    
#myobj = myit()
#itr = iter(myobj)
#print(next(itr))        
#print(next(itr))     


#_____________________________________________generators____________________________________
#def test():
 #   yield 4

#y = test()
#print(next(y))



#def test(a):
 #   for i in a:
  #      yield i

#y = test([2,4,6,8])
#print(next(y))
#print(next(y))
#print(next(y))

#_________figonachi series________
#def fib():
#    a,b = 0,1

 #   while True:
  #      c = a+b
   #     yield a
    #    a,b=b,c

#y = fib()
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))

#_____________________________________________multithreading____________________________________
#_______1
#import threading                #running the program commands simultaneously
#from time import sleep
#def func1():
 #   for i in range(15):
  #      print('good')
   #     sleep(1)
#def func2():
 #   for i in range(15):
  #      print('Bye')
   #     sleep(2)
#t1 = threading.Thread(target=func1)
#t2 = threading.Thread(target=func2)

#t1.start()
#sleep(0.2)
#t2.start()

#_______2
#from threading import *
#from time import sleep

#class A(Thread):
 #   def run(self):
  #      for i in range(5):
   #         print('hello', current_thread().getName()) #curent_thread...... is used to get the thread of that relavant executing thing
    #        sleep(1)
#class B(Thread):
 #   def run(self):
  #      for i in range(5):
   #         print('world', current_thread().getName()) #curent_thread...... is used to get the thread of that relavant executing thing
    #        sleep(2)
#obj1 = A()
#obj2 = B()
#obj1.start()
#sleep(0.2)
#obj2.start()
#obj1.join() #to put bye in the end
#obj2.join() #to put bye in the end
#print('bye', current_thread().getName()) #curent_thread...... is used to get the thread of that relavant executing thing

#_______3
#from threading import *
#from time import *

#lock = Lock()
#def display():
 #   lock.acquire() #to run one thread after finishing one thread
  #  for i in range(5):
   #     print(current_thread().name)
    #    sleep(1)
    #lock.release()
#t1 = Thread(target=display)
#t2 = Thread(target=display)
#t1.start()
#t2.start()


#_____________________________________________abstract class____________________________________
#from abc import ABC, abstractmethod         #used to use an empty class just for inheritance

#class phone(ABC):
 #   @abstractmethod
  #  def func(self):
   #     pass
    
#class samsung(phone):
 #   def func(self):
  #      pass
    
#obj1 = samsung()




#_____________________________________________file handling____________________________________
#________Read________
#x = open("text file.txt", "r")
#print(x.read())
#print(x.readline(), end='') #end= is used to remove the additional space aded
##print(x.readline())
#print(x.readlines()) # put the lines in a list
#x.close()

#with open('text file.txt', 'r') as x: #with this no need to close this
#    print(x.read())

#________write________
#x = open('text file.txt', 'w')
#x.write('Hello\n')
#x.write('world')
#x.close

#________append________
#x = open('text file.txt', 'a')
#x.write('\nramiru liyanage')
#x.close()

#________creatinf file________
# = open('hello.txt', 'w') #can creaete files if file doesnt exit
#x.write('hello')

#________image handling________
#x = open('exam cert. status code.png', 'rb')
#print(x.read())


#________OS module________
#import os
#os.remove('hello.txt') #remove a file
#os.rename('hello.txt', 'test.txt') #to rename a file (can be done for folders too)
#print(os.path.exists('test.txt')) #to check if file exits
#print(os.path.abspath('test.txt')) #to see where the file is
#print(os.path.getsize('test.txt')) #to see how many elements are there in the file

#import os
#print(os.getcwd()) #get directory location
#os.chdir(r'C:\Users\Ramiru\Downloads\path 1\path 2\module learning test') #changing directory location 
#print(os.getcwd())
#os.chdir(r'C:\Users\Ramiru\Documents\Pre engineering\Programming\modules learning')
#print(os.getcwd())
#print(os.listdir()) #to get all the files and folders on that directory

#os.mkdir('created through vs code python/python') #to create a new folder (/ptyhon = to create a sub folder inside)
#os.mkdir('made for deleting process') 
#os.rmdir('made for deleting process') #to delete a folder
#os.mkdir('made for deleting process 1/python') #to delete a sub folder
#os.rmdir('made for deleting process 1/python')
#os.rmdir('made for deleting process 1')

#_____help
#import os
#print(dir(os))
#print(len(dir(os)))
#print(help(os.join))

#___________________________everything done here can be used for both files and folders


#_____________________________________________random numbers____________________________________
#import random
#x = random.random() #print any random number
#print(x)
#x = random.random() *10 #print random numbers with whole number part
#print(x)
#x = random.uniform(1,10) #print random numbers between 1 to 10
#print(x)
#x = random.randint(5,10) #print random integers between 1 to 10
#print(x)

#import random
#name = ['kamal', 'amal', 'saman']
#print(random.choice(name)) #choosing an element randomly
#print(random.choices(name, k=2)) #choosing two names randomly


#import random
#numbers = list(range(1,10))
#print(numbers)
#random.shuffle(numbers) #to shuffle elements in a list
#print(numbers)


#_____________________________________________zip function____________________________________
#names = ['kamal', 'amal', 'saman']
#ages = [34, 56, 20]
#marks = [99, 57, 45]

#details = dict(zip(names, ages)) #cant print dictionaries after zipping more than 2 lists
#print(details)
#details = tuple(zip(names, ages, marks)) #to pair up different tuples together
#print(details)
#details = list(zip(names, ages, marks)) #to pair up different lists together
#print(details)

#unzip = list(zip(*details)) #to unzip a zipped list (can be used for tuples and dictioneries too)
#print(unzip)







#_____________________________________________creating patterns____________________________________
#_______ascending_______
#for i in range(int(input('enter number: '))):
#    for j in range(i + 1):
 #       print('*', end='')
  #  print()
#_______descending_______
#n = int(input('enter number: '))
#for i in range(n):
 #   for j in range(n -i):
  #      print('*', end='')
   # print()

#_______pyramid_______
#n = int(input('enter number: '))
#for i in range(n):
 #   for j in range(n-i-1):
  #      print(' ', end='')
   # for k in range(2*i+1):
    #    print('*', end='')
    #print()


#_______heart_______







































































































































































































































































































