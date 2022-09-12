#set{} / Useful for mathematical calculation like union, intersection, symmetric difference, etc../ It won't take duplicate value, 
# It will delete duplicate value automatically 
# / It will print randomly / We can add, & remove the value
# Set is a collection which is unordered and unindexed. No duplicate members

print("Set Type: Set & Frozenset \n"); print("Set Example")
data2 = {"Arabic", "Tamil", "Telugu", "Malayalam", "Urdu", "Kannada"}; print(data2)
data2.add("English"); print(data2) # Adding the value
data2.update(["French", "German, Chinese"], {1,2,3,2,3,1}); print(data2) # To add multiple values
data2.remove("Telugu"); print(data2) # Removed the Value "Telugu" It won't support the index value like remove[1] / We can use remove or discard
# Difference between discard & remove. In discard if you delete non-present values it won't show any error, But in remove it will show the error message
print("\n")
data2.discard(1); print(data2) #By using discard we removed
data2.add("Tamil"); print(data2) # Again we added "Tamil" But it will removed duplicate
data2.clear(); print(data2) #It will delete all the value
#del data2 / It will delete the data2 variable
data3 = {100,20,55,90,128,9773,3238} ; print(data3)
my_set = dict(); my_set = {}; print(type(my_set)) # By defaullt it will take class 'dict' / dict() or {} both are class dict
my_set = set(); print(type(my_set)) # So we need to create empty set like this / {} it's not set so we need to set like this set()

print("\n" "Set Operation: Set Union (|), Set Intersection (&), Set Difference (-), Set Symmetric Difference (^),")

print("\n")
print("Set Union (Symbol is |) - It will add A & B and not repeat the duplicate value that means it won't repeat the elements / Example Below")
A={1,2,3,4,5}
B={4,5,6,7,8} #All elements printed and no elements is repeated. 1,2,3,4,5,6,7,8
print(A|B)

print("Set Intersection (Symbol is &) - contains all the elements that are common to both the sets / Example Below")
A={1,2,3,4,5}
B={4,5,6,7,8} #contains all the elements that are common to both the sets 4, 5
print(A&B)

print("Set Difference (Symbol is -) - The difference of two sets, written A - B is the set of all elements of A that are not elements of B / Example Below")
A={1,2,3,4,5}
B={4,5,6,7,8} #The difference of two sets, written A - B is the set of all elements of A that are not elements of B 1,2,3
print(A-B)

print("Set Symmetric Difference (Symbol is ^) - The symmetric difference of the sets A and B are those elements in A or B, but not in both A and B / Example Below")
A={1,2,3,4,5}
B={4,5,6,7,8} #The symmetric difference of the sets A and B are those elements in A or B, but not in both A and B 1,2,3,6,7,8
print(A^B)
A.add(10)
B.update({10,11})
print(A^B) # Output 1,2,3,6,7,8,11

print("\n" "Set Membership Test: Membership test is a query with an outcome of True or False, determining whether an item is in a given set or not./ Example Below")
myset = set("apple")
print('a' in myset) # Output True
print('b' in myset) # Output False

print("\n" "Iteration: iterator() method is used to return an iterator of the same elements as the set/ Example Below")
my_set = ([1,2,3,4,5])
print(my_set)
print(my_set[0])
print(type(my_set))
for x in my_set:
 print(x)
 
print("\n" "Frozenset: Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation / In set we used symbols but in frozenset is we can use symbol as well as (For union (union) copy (copy) intersection (intersection),  Example Below")

A=frozenset([1,2,3,])
print(A)
# A.add(4) you can't able to add 4 bcos it's frozenset
print(type(A))
a=frozenset() #Empty frozenset
print(a)

#Copy
C=A.copy()
print(C)

