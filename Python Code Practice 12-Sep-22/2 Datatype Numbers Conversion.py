# Data Types / Python Numbers / Type Conversion / Casting (Specify a Variable Type)

""" 
Built-in Data Types / Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

#Getting the Data Type (You can get the data type of any object by using the type() function: / Print the data type of the variable x: )
x = 5
print(type(x))

#Setting the Data Type
"""
In Python, the data type is set when you assign a value to a variable:
        Example	                                        Data Type
x = "Hello World"	                                        str	
x = 20	                                                    int	
x = 20.5	                                                float	
x = 1j	                                                    complex	
x = ["apple", "banana", "cherry"]	                        list	
x = ("apple", "banana", "cherry")	                        tuple	
x = range(6)	                                            range	
x = {"name" : "John", "age" : 36}	                        dict	
x = {"apple", "banana", "cherry"}	                        set	
x = frozenset({"apple", "banana", "cherry"})	            frozenset	
x = True	                                                bool	
x = b"Hello"	                                            bytes	
x = bytearray(5)	                                        bytearray	
x = memoryview(bytes(5))	                                memoryview	
x = None	                                                NoneType
"""

#Setting the Specific Data Type
"""
    Example	                                            Data Type
x = str("Hello World")	                                  str
x = int(20)	                                              int	
x = float(20.5)	                                        float	
x = complex(1j)	                                         complex	
x = list(("apple", "banana", "cherry"))	                list	
x = tuple(("apple", "banana", "cherry"))	            tuple	
x = range(6)	                                        range	
x = dict(name="John", age=36)	                         dict	
x = set(("apple", "banana", "cherry"))	                set	
x = frozenset(("apple", "banana", "cherry"))	        frozenset	
x = bool(5)                                         	bool	
x = bytes(5)	                                        bytes	
x = bytearray(5)	                                    bytearray	
x = memoryview(bytes(5))	                            memoryview
"""

#Numeric Types
"""There are three numeric types in Python:
int
float
complex
Variables of numeric types are created when you assign a value to them:
Example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

Complex
Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
"""

# Type Conversion (You can convert from one type to another with the int(), float(), and complex() methods:)
#Example : Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Python Casting
# Example Int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Example Float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Example String
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
