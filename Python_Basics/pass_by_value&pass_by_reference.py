

# 7️⃣ Python এ pass by value এবং pass by reference কি?
# পাইথনে একে বলা হয় Pass by Object Reference।

# যদি অবজেক্ট Mutable (যেমন List) হয়, তবে ফাংশনের ভেতর পরিবর্তন করলে অরিজিনাল ডাটাও চেঞ্জ হবে।
# যদি অবজেক্ট Immutable (যেমন String) হয়, তবে অরিজিনাল ডাটা চেঞ্জ হবে না।

# Mutable
def change_list(list):
   list.append(4)

my_list = [1, 2, 3]
change_list(my_list)
print(my_list) 

# Immutable 
def change_string(string):
   string += "World"
   return string

my_string = "Hello"
print(change_string(my_string))
print(my_string)

my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, )
print(f"Original Tuple: {my_tuple}")
print(f"New Tuple: {new_tuple}")


################################################

# 1. Modify a Mutable Object
def update_list(my_list):
   my_list.append(4)

numbers = [1, 2, 3]
update_list(numbers)
print(numbers)


# 2. Dictionary Mutable
def update_dict(my_dict):
   my_dict["Key"] = "value"

person = {"name": "Mamun"}
update_dict(person)
print(person)


# 3. Immmutable String
def change_string(s):
   s = s + "World"
   print("Inside:", s)

text = "Hello"
change_string(text)
print("Outside:", text)


# 4. Immutable Tuple
def change_tuple(t):
   t = t + (4, )
   print("Inside:", t)

my_tuple = (1, 2, 3)
change_tuple(my_tuple)
print("Outside:", my_tuple)


# 5. Mutable but Reassignment
def reassign_list(list):
   list = [4, 5, 6]
   print("Inside:", list)

my_list = [1, 2, 3]
reassign_list(my_list)

print("Outside:", my_list)


# 6. Tuple inside a list
def modify_tuple(data):
   data[0] = 100

my_data = [1, (3, 4)]
modify_tuple(my_data)
print(my_data)


# 7. Copy vs Reference
def modify_list(list):
   list.append(4)

a = [1, 2, 3]
b = a # b is reference to a 
modify_list(b)
print(a)

# Fix using copy
import copy
a = [1, 2, 3]
b = a.copy()

b.append(4)
print(a)
print(b)

# "Python doesn't use pure pass by value or pass by reference.
# It uses pass by object reference."
# Immutable → new object → original unchanged
# Mutable → same object → original changed
# Modify করলে → change হবে
# Reassign করলে → change হবে না