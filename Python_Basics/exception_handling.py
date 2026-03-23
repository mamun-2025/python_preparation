
# 8️⃣ Python এ exception handling কিভাবে করা হয়?
# পাইথনে try, except, else, এবং finally ব্লক ব্যবহার করে এরর হ্যান্ডেল করা হয়।

# try:
#    x = 10/0
# except ZeroDivisionError: # Error handle 
#    print("Cannot divide by zero!")
# else:                     # If no error occurs, this block will execute
#    print("Division successful.")
# finally:                  # This block will always execute.
#    print("This will always execute.")


# 1.Multiple exception handle
try:
   x = 10 / 0
except ValueError:
   print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
   print("Cannot divide by zero!")



# 2. Multiple exception in one block
try:
   x = int("abc") # This will raise a ValueError
except (ValueError, TypeError):
   print("An error occurred! Please check your input.")


# 3. Ussing else
try:
   x = int(10 / 2)
except ZeroDivisionError:
   print("Canno divide by zero!")
else:       # ese block will excute if no exception occurs in the try block
   print("Division successful. Result:", x)


# 4. Using finally 
try:
   x = 10 / 5
except ZeroDivisionError:
   print("Cannot divide by zero!")
finally: # finally block will always execute if an exception error occurs or not
   print("This will always execute.")


# 5. Exception Object of catching method
try:
   x = 10 / 0 
except Exception as e: # Exception class of object e will catch any exception that occurs in the try block
   print("An error occurred:", e)


# 6. Custom Exception of raising method
def check_age(age):
   if age < 18:
      raise ValueError("Age must be at least 18.")
   return "Age is valid."

print(check_age(20))
# print(check_age(15)) 


# 7. Custom Exception of creating method
class CustomError(Exception):
   pass 

def test():
   raise CustomError("This is a custom error!")

try:
   test()
except CustomError as e:
   print(e)


# 8. Nested try-except block
try:
   x = 10 / 0 
   try:
      y = int("abc")
   except ValueError:
      print("Inner exception: Invalid input!")
      raise # Again throw the exception to outer block
except ZeroDivisionError:
   print("Outer exception: Cannot divide by zero!")


# 9. File handling with exception
try:
   with open("data.txt") as f:
      conent = f.read()
except FileNotFoundError:
   print("File not found! Please check the file path.")

# ১. try-except এর কাজ
# try: এই ব্লকের ভেতরে আমরা সেই কোডটুকু লিখি যেটিতে ভুল বা এরর হওয়ার সম্ভাবনা থাকে।
# except: যদি try ব্লকের কোডে কোনো ভুল হয়, তবে প্রোগ্রামটি বন্ধ না হয়ে সরাসরি except ব্লকে চলে আসে এবং সেখানে থাকা নির্দেশাবলী পালন করে।

# ২. Multiple Except, Else এবং Finally
# আপনি আপনার কোডে যেভাবে ব্যবহার করেছেন, সেটির কাজ নিচে দেওয়া হলো:
# Multiple Except: একটি মাত্র try ব্লকের জন্য আমরা আলাদা আলাদা এরর (যেমন: ValueError, ZeroDivisionError) ধরার জন্য একাধিক except ব্লক ব্যবহার করতে পারি।
# Else: যদি try ব্লকের কোডটি কোনো এরর ছাড়াই সফলভাবে চলে, তবেই কেবল else ব্লকটি কাজ করবে।
# Finally: এরর হোক বা না হোক, এই ব্লকের কোডটি সব সময় (Cleanup এর জন্য) রান করবে।

# ৩. Custom Exceptions এবং Raise
# raise: পাইথনে আমরা নিজেরা ইচ্ছা করে কোনো নির্দিষ্ট শর্তে এরর তৈরি করতে পারি raise কীওয়ার্ড ব্যবহার করে। একে কাস্টম এক্সেপশন বলা হয়। 
# যেমন—ব্যবহারকারীর বয়স যদি ১৮-র কম হয়, তবে আমরা একটি এরর raise করতে পারি।