
# 🔟 Python এর with statement কেন এবং কিভাবে ব্যবহার হয়?
# এটি মূলত Resource Management-এর জন্য ব্যবহৃত হয় (যেমন ফাইল ওপেন করা)। 
# এর সুবিধা হলো কাজ শেষ হওয়ার পর এটি অটোমেটিক ফাইল বা কানেকশন ক্লোজ করে দেয়, এমনকি এরর হলেও।
# file close করতে ভুল হতে পারে
# error হলে file open থেকে যায়
# ✅ Solution:
# 👉 with → automatic cleanup

# with statement 
with open('file.txt', 'w') as file:
   file.write("Hello, World!")


# without with statement
file = open('without_with.txt', 'w')
file.write("Hello, World!")
file.close()


# 1. Reading file
# with open('read.txt', 'r') as file:
#     content = file.read()
#     print(content)


# 2. Mutiple Context Managers
with open('file1.txt', 'w') as file1, open('file2.txt', 'w') as file2:
    file1.write("This is file 1.")
    file2.write("This is file 2.")


# 3. Exception handlind with with
try:
    with open('data.txt') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the file name and path.")


# 4. Custom Context Manager
class CustomContext:
   def __enter__(self):
        print("Entering the context.")
        return self
   def __exit__(self, exc_type, exc_value, traceback):
         print("Existing the context.")

with CustomContext() as obj:
    print("Inside the context.")


# 5. Using contextlib for custom context manager
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering the context.")
    yield
    print("Existing the context.")

with my_context():
    print("Working inside the context.")


# 6. File handling with error handling
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
      print("File not found. Please check the file name and path.")


# 7. Database connection

class DatabaseConnection:
   def __enter__(self):
         print("Connecting to the database.")
         return self
   def __exit__(self, exc_type, exc_value, traceback):
         print("Database connection closed.")

with DatabaseConnection() as db:
    print("Performing database operations.")
      
    