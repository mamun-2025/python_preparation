
# Lambda Function কি?
# ✅ Definition: Lambda function হল একটি ছোট anonymous function যা এক লাইনে লেখা হয় এবং সাধারণত একটি এক্সপ্রেশন রিটার্ন করে। এটি `lambda` কীওয়ার্ড দিয়ে তৈরি করা হয়।
# ✅ Syntax: 
# lambda arguments: expression

# 1. Normal Function
def add(x, y):
   return x + y

print(add(5, 3))

# 2. Lambda Function
add_lambda = lambda x, y: x + y 
print(add_lambda(5, 3))

# 3. One-liner lambda function 
print((lambda x, y: x * y) (4, 5))



# Lambda কেন ব্যবহার করা হয়?
# 👉 Short code লিখতে
# 👉 temporary function হিসেবে
# 👉 functional programming (map, filter, sorted)

# 4. Lambda with map function
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))
print(result)


# 5. Lambda with filter function
numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


# 6. Lambda with sorted function(interview favorite)
names = ['Mamun', 'Arafat',  'Jhonnnny', 'Sakib', 'Rafiq']

sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)

students = [("Mamun", 26), ("Arafat", 24), ("Sakib", 28), ("Rafiq", 22)]

students.sort(key=lambda x: x[1])
print(students)

# 🧠 কখন ব্যবহার করবা?
# 👉 Use Lambda when:
# simple logic (1 line)
# temporary function দরকার
# map, filter, sorted use করো

# ⚠️ Limitations

# ❌ multiple statement লিখা যায় না
# ❌ complex logic করা যায় না

# 7. Real-life example
products = [
   {"name": "Laptop", "price": 50000},
   {"name": "Smartphone", "price": 30000},
   {"name": "Watch", "price": 5000}
]

products.sort(key=lambda x: x['price'])
print(products)

# "Use lambda for short, simple, one-time functions."

