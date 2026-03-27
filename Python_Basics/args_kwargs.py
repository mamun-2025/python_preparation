
# 6️⃣ Python এ *args এবং **kwargs কি?
# *args → positional arguments এর জন্য (tuple হিসেবে collect হয়)
# *args: এটি ফাংশনে অনির্দিষ্ট সংখ্যক পজিশনাল আর্গুমেন্ট পাস করতে ব্যবহৃত হয় (টাপল হিসেবে রিসিভ করে)।

# **kwargs → keyword arguments এর জন্য (dict হিসেবে collect হয়)
# **kwargs: এটি কি-ওয়ার্ড আর্গুমেন্ট (Key-Value) পাস করতে ব্যবহৃত হয় (ডিকশনারি হিসেবে রিসিভ করে)।


# 1.Basic Example of Multiple Positional Argument (*args)
def add_numbers(*args):
   total = 0
   for num in args:
      total += num 
   return total

print(add_numbers(1, 2, 3, 4))
print(add_numbers(10, 20, 30))
# *args → unlimited positional arguments নেয়
# function call করার সময় যত খুশি value দিতে পারো


# 2. Basic Example of Multiple Keyword Argument (**Kwargs)
def user_info(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}: {value}")

user_info(name="Mamun", age=30, city="Bangladesh", blood_group="B+")
# **kwargs → key=value আকারে data নেয়
# dictionary হিসেবে কাজ করে


# 3. *args and **kwargs together
def mix_example(a, b, *args, **kwargs):
   print("a:", a)
   print("b:", b)
   print("args:", args)
   print("kwargs:", kwargs)

mix_example(1, 2, 3, 4, 5, name="Mamun", age=30, role="junior_backend_developer")


# 4. Unpacking with *args and **kwargs
def unpack_example(a, b, c):
   print(a, b, c)

unpack_list = [1, 2, 3]
unpack_example(*unpack_list)

unpack_dict = {"a": 10, "b": 20, "c": 30}
unpack_example(**unpack_dict)


# 5. Default values with *args and **kwargs
def default_example(a, b=10, *args, **kwargs):
   print("a:", a)
   print("b:", b)
   print("args:", args)
   print("kwargs:", kwargs)

default_example(1, 20, 3, 4, name="Mamun", age=30)


# 6. Logger function with *args and **kwargs
def log(message, *args, **kwargs):
   print("Log Message:", message)

   if args:
      print("Extra Positional Arguments:", args)
   
   if kwargs:
      print("Extra Keyword Arguments:", kwargs)

   if not args and not kwargs:
      print("Meta Information:")

log("User logged in", 123, 321, name="Mamun", role="junior_backend_developer", location="Bashundhara Residential Area")
