
# 5️⃣ Python এ variable type কিভাবে চেইঞ্জ হয়?

# Python dynamically typed, তাই variable type runtime এ change করা যায়।
# পাইথন একটি Dynamically Typed ল্যাঙ্গুয়েজ। 
# অর্থাৎ ভ্যারিয়েবল ডিক্লেয়ার করার সময় টাইপ বলে দিতে হয় না এবং রানটাইমে এটি পরিবর্তন হতে পারে।

# Example 1:
x = 5
x = "Hello"
x = [1, 2, 3]
x = {'name': "Mamun", 'age': 27}
x = True 
x = 3.14
print(x)

# Example 2:
y = 10
print(type(y))

y = "python"
print(type(y))

y = [1, 2, 3]
print(type(y))

y = (1, 2, 3)
print(type(y))

y = {1, 2, 3}
print(type(y))

y = {'name': 'Mamun', 'age': 27}
print(type(y))

y = True 
print(type(y))