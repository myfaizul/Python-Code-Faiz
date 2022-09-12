# Escape Characters
                    
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

#Example:You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north." (We will get syntax error)

# To fix this problem, use the escape character \":
#Example: The escape character allows you to use double quotes when you normally would not be allowed:
#txt = "We are the so-called \"Vikings\" from the north."

# Escape charater : It will run that functionallity 

# escape characters are --> \a (Question mark symbol) \n (new line) \r  (Carriage return) \t (Tab) \' (Single Quote) \" (Double Quote) \\ (Back Slash) \b (Back Space) \f (Form Feed) \ooo (Octal Value) \xhh (Hex Value)

#What is the difference between \r and \n?
#They're different characters. \r is carriage return, and \n is line feed. On "old" printers, \r sent the print head back to the start of the line, and \n advanced the paper by one line. Both were therefore necessary to start printing on the next line.

print ("\a") # Some kind of question mark symbol coming
print ("\n") # Next line i,e new line printed

print ('Faizul')

print("\t Ahamed") # Tab space (4 space)

#Practice

print("\n \n \n") # Three new line
print ("Faizul\a \n \t \a")
print ("Faizul" "\t Ahamed")
print('Faiz \r Ahamed \r \'Shayan\'')
print('\r Talha')
print('\r Hunain')
print('Tameez')

#A backslash followed by an 'x' and a hex number represents a hex value: 4 repreent capital 6 represent small letter.
#Hexadecimal is a numbering system with base 16. It can be used to represent large numbers with fewer digits. In this system there are 16 symbols or possible digit values from 0 to 9, followed by six alphabetic characters -- A, B, C, D, E and F.

txt = "\x48\x65\x6c\x6c\x6f" # out put Hello
print(txt) 

txt1 = "\x46\x61\x69\x6f"
print(txt1)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) # out put Hello

