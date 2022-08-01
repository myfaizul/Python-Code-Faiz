a = 'Name'  #global variable
b =  'Age'  #global Variable
def myfunc():
    global a #In Local we assign the global , So it will take 10 is the global value
    a = 10
    print(a)
myfunc()

print(a)