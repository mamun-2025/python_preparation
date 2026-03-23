

# 9️⃣ Python এ List Comprehension এবং Dictionary Comprehension কি?
# List Comprehension: list তৈরি করার short way
# Dict Comprehension: dictionary তৈরি করার short way
# লিস্ট এবং ডিকশনারি কমপ্রিহেনশন হলো পাইথনে এক লাইনের কোড ব্যবহার করে নতুন লিস্ট বা ডিকশনারি তৈরি করার একটি সংক্ষিপ্ত পদ্ধতি। 
# এটি সাধারণ for loop ব্যবহারের তুলনায় কোডকে আরও ছোট, সুন্দর (Readable) এবং দ্রুত (Performance) করে তোলে।
# চিরাচরিতভাবে একটি লিস্ট তৈরি করতে গেলে আমাদের কয়েক লাইন কোড লিখতে হয়। 
# কিন্তু কমপ্রিহেনশন ব্যবহার করে তা এক লাইনেই সম্ভব।


# Tradition way of creating a list
squares = []
for x in range(10):
   squares.append(x**2)

print(squares)

# List Comprehension way of creating a list 
squares = [x**2 for x in range(5)]
print(squares)


# 1. With Condition in filtering
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)


# 2. If-Else inside Comprehension
results = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(results)


# 3. Nested loop in Comprehension
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)

# 4. Flatten a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print(flattened)


# 5. Dictionary Comprehension 
squares_dict = {x: x**2 for x in range(5) if x % 2 == 0}
print(squares_dict)


# 6. Transform a dictionary
data = {"a": 1, "b": 2, "c": 3}

new_data = {key: value**2 for key, value in data.items()}
print(new_data)

# 7. Swape key-vlaue in a dictionary
data = {"a": 1, "b": 2, "c": 3}

swapped = {value: key for key, value in data.items()}
print(swapped)

# 8. Set Comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)

# 9. Real life example of list comprehension
users = [
   {"name": "Mamun", "age": 25},
   {"name": "Rahim", "age": 20}
]

user_names = [user["name"] for user in users]
print(user_names)
user_names = [user["name"].upper() for user in users if user["age"] > 21]
print(user_names)
user_names = [user["name"].upper() if user["age"] > 21 else user["name"].lower() for user in users]
print(user_names)

# 10. Golder rule
# simple rule : use Comprehension
# Comple rule: Use Loop 
