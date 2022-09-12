# Python String / Slicing Strings / Modify Strings / Concatenation String  / Format String / Escape Characters

"""Python Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
You can display a string literal with the print() function:
Example:
print("Hello")
print('Hello')

Assign String to a Variable
a = "Hello"
print(a)"""

#Multiline Strings:
#You can assign a multiline string to a variable by using three quotes:
#Example: You can use three double quotes:
a = """Faizul Ahamed
Shayan Talha
Ziya
Hunain
Faizoon
"""
print(a)

#Or three single quotes:
b = '''Faizul Ahamed
Shayan Talha
Ziya
Hunain
Faizoon
'''
print(a)

#Slicing Strings
# Slice From the Start 
"""By leaving out the start index, the range will start at the first character:
Example
Get the characters from the start to position 5 (not included):"""
b = "Hello, World!"
print(b[:5])

#Slice To the End
"""By leaving out the end index, the range will go to the end:
Example
Get the characters from position 2, and all the way to the end:"""
b = "Hello, World!"
print(b[2:])

#Negative Indexing
"""Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):"""
b = "Hello, World!"
print(b[-5:-2])

#Modify Strings
#Python has a set of built-in methods that you can use on strings.
#Upper Case
"""Example
The upper() method returns the string in upper case:"""
a = "Hello, World!"
print(a.upper())

#Lower Case
"""Example
The lower() method returns the string in lower case:"""
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
"""Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
Example: The strip() method removes any whitespace from the beginning or the end:"""

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
"""Example
The replace() method replaces a string with another string:"""
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
"""The split() method returns a list where the text between the specified separator becomes the list items.
Example: The split() method splits the string into substrings if it finds instances of the separator:"""
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#String Concatenation
"""To concatenate, or combine, two strings you can use the + operator.
Example: Merge variable a with variable b into variable c:"""
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
"""As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

But we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
Example
Use the format() method to insert numbers into strings:"""

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape Characters
"""You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north.

To fix this problem, use the escape character \":
The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
"""
#Other escape characters used in Python:
"""
Code	        Result
\'	        Single Quote	
\\	        Backslash	
\n	        New Line	
\r	        Carriage Return	
\t	        Tab	
\b	        Backspace	
\f	        Form Feed	
\ooo	    Octal value"""	
# \xhh	    Hex value

