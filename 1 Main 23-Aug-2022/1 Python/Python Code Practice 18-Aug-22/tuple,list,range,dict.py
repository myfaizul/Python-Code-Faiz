print("Sequence Type: Tuple, List and Range \n")
#Tuple () / Here we can't able to delete or modify the values But we can add the values / Only delete the variable
#Tuple is a read only data structure as we can't modify the size and value of the items of a tuple

print ("Tuple Example")
data = ("Value1", "Value2", 21.0, 25, "Main") ; print(data)
data = data + ("Master",); print(data) # Adding the value "Master"

print (data[2]) # It will print the value 2 (21.0)
print (data[0]) # It will print the value 0 (Value1)
#del data (It will delete the variable "data")
print("\n") #New Line


#List [] / It's easy / Here we can add, modify & delete the values
print ("List Example")
data1 = ["Item1", "Item2", 100, 121.5, "Grocery"] ; print(data1)
data1.append("Monthly"); print(data1) # Adding the value "Monthly"
data1[4] = "Yearly"; print(data1) #Modify the value "Grocery to Yearly"
del data1[4]; print(data1) # Deleted the value 4
del data1[1:100]; print(data1) #It will delete the value between 1 to 100 except 0

print("\n")
print("Range Example")
# del data1 / If we want sequence of number from 1 to 10, we need use the range function like this range(1, 11) 
# Here start of the sequence is inclusive but the end is exclusive) / The range function return a range objects 
# which is the sequence of characters 

result = range(1,11)
print(result) #Out put is 1,11
result1 =range(11) # Output is 0, 11
print(result1)
print(list(result)) # if we convert it to some other type it will print from 1 to 10
print(list(result1)) # Out put is 0, to 10
for value in range (0, 6):
 print(value, "repeating") #repeating printing 6times from 0 to 5 value
for value in range(4):
  print(value)


#range() with only stop parameter


print("\n")

#Range() / It will return a range object which is a sequence of characters

# Dict {:}
print("Mapping Type: Dictionary or Dict \n"); print("Dict Example")
employee = {"Faizul" : "ID2121", "Shayan" : "ID2122"}; print(employee)
#Faizul is keys & ID2121 is values
print(employee.keys()) # It will print only keys
print(employee.values()) # It will print only values
employee["Hunain"] = "ID2123" ; print(employee)
print(employee["Faizul"]) #It will display the Partcular keys value
# print(employee["ID2122"]) #We can't find the keys by using value, Only by using keys we will find value
print("\n")

#Another example for single keys with multiple values
employee1 = {

"Shahul" :["ID0001","Age-25", "City-Pollachi"],
"Fahima" :["ID0002", "Age-22", "City-Palakkad"]
}
print(employee1["Shahul"][0:5]) #or print(employee1["Shahul"][1])
emp=employee1["Shahul"][1]
print("Shaul Age is" ,emp)
print("ID00001 Age is", emp)
print("\n")



