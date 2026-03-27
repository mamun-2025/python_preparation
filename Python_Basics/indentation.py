
# 4️⃣ Python এর indentation কেন গুরুত্বপূর্ণ?

# Python code block define করার জন্য curly braces নেই, তাই indentation দিয়ে structure define করতে হয়।
# অন্যান্য ল্যাঙ্গুয়েজে কার্লি ব্র্যাকেট {} ব্যবহার হলেও পাইথনে Code Block বোঝাতে ইনডেন্টেশন (সাধারণত ৪টি স্পেস) বাধ্যতামূলক। 
# এটি কোডকে আরও রিডেবল করে। 
# ইনডেন্টেশন ঠিক না থাকলে IndentationError দেখা দেয়।

# Exampe of correct intdentation
x = 10
if x > 5:
   print("x is greater than 5")

# Example of incorrect indentation 
x = 10 
if x > 5:
# print("x is greater than 5") # This will raise an IndentationError