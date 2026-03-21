
# 2️⃣ Python এর mutable এবং immutable data types কি কি?

# Mutable: পরিবর্তনযোগ্য (changeable) → List, Dictionary, Set
# Mutable: যেগুলোর ভ্যালু পরিবর্তনের সুযোগ থাকে (যেমন: List, Dictionary, Set)।

# Immutable: অপরিবর্তনীয় (unchangeable) → Tuple, String, Integer, Float
# Immutable: যেগুলোর ভ্যালু একবার ডিফাইন করলে আর পরিবর্তন করা যায় না (যেমন: int, float, string, tuple)।

# Mutable data 
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Immutable data 
my_tuple = (1, 2, 3)
# my_tuple.append(4)  # This will raise an AttributeError
print(my_tuple)