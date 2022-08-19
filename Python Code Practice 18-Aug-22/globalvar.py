car = 'Hyundai'  #global variable
color = 'Grey'  #global Variable
def myfunc():
    global car #In Local we assign the global car is maruti in outside global is hyndai , once you assign global var in local. That will be fixed
    car = "Maruti"
    print(car)
myfunc()

print(car) # it not call the outside global varibale / it's take the inside assigned global function
print(color)