"""
Indentation / Variable / Casting / Tyep Of Function / Legal & Illegal variable Name / Multiword Variable Name(Camel, Pascal, Snake Case) / 
Many Values to Multiple Variables / One Value to Multiple Variables / Unpack a Collection / Output Variables / Global Variables

"""

# Indentation (The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one)
if 5 > 2:
  print("Five is greater than two!")

  if 2 < 4:
  #print("Two is less than 4!") If we remove # it will be error so need to give proper space
    print("Two is less than 4! \n")

#if 5 > 2:
#print("Five is greater than two!") Minimum one space is required else we will get IdentationError

# Variables (Python has no command for declaring a variable / A variable is created the moment you first assign a value to it.)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting: If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y),"\n")

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John" """

"""Multi Words Variable Names (Variable names with more than one word can be difficult to read/ 
There are several techniques you can use to make them more readable:)

Camel Case: Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case: Each word starts with a capital letter:
MyVariableName = "John"

Snake Case: Each word is separated by an underscore character:
my_variable_name = "John"
"""

#Many Values to Multiple Variables (Python allows you to assign values to multiple variables in one line)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z,"\n")

#One Value to Multiple Variables (And you can assign the same value to multiple variables in one line:)
x = y = z = "Orange"
print(x)
print(y)
print(z,"\n")

# Unpack a Collection (If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. 
# This is called unpacking.) / Example : Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables : The Python print() function is often used to output variables.
x = "Python is awesome"
print(x,"\n")

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z,"\n")

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

x = 5
y = 10
print(x + y)

#x = 5
#y = "John"
#print(x + y) (Error)

x = 5
y = "John"
print(x, y,"\n")

car = 'Hyundai'  #global variable
color = 'Grey'  #global Variable
def myfunc():
    global car #In Local we assign the global car is maruti in outside global is hyndai , once you assign global var in local. That will be fixed
    car = "Maruti"
    print(car)
myfunc()

print(car) # it not call the outside global varibale / it's take the inside assigned global function
print(color)
