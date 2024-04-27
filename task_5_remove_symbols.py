'''
The goal is to remove unnecessary symbols from the string str = "Py123Ladies123" but AT LEAST in two different ways.
There are many more options to do it. Get creative (don't hesitate to use google)
and share with us later how many ways you found to solve this problem! 
'''

string = "Py123Ladies123"
print(f"Original string: {string}")

# 1st way
string_cleaned = string.replace("123","")
print(f"01st way: {string_cleaned}")

# 2nd way
import re
string_cleaned = re.sub("[0-9]", "", string)
print(f"02nd way: {string_cleaned}")

# 3rd way
string_cleaned = "".join([i for i in string if not i.isdigit()])
print(f"03rd way: {string_cleaned}")

# 4th way
string_cleaned = "".join([i for i in string if i.isalpha()])
print(f"04th way: {string_cleaned}")

# 5th way
f = filter(str.isalpha, string)
string_cleaned = "".join(f)
print(f"05th way: {string_cleaned}")

# 6th way
import re
string_cleaned = re.sub("[^a-zA-Z]", "", string)
print(f"06th way: {string_cleaned}")

# 7th way
string_cleaned = "".join(i for i in string if not i.isdecimal())
print(f"07th way: {string_cleaned}")

# 8th way
for i in range(10):
    string = string.replace(str(i), "")
string_cleaned = string
print(f"08th way: {string_cleaned}")

# 9th way
import re
string_cleaned = re.sub(r'\d+', '', string)
print(f"09th way: {string_cleaned}")

 # 10th way
string_cleaned = ''
for char in string:
   if not char.isdigit():
       string_cleaned += char
print(f"10th way: {string_cleaned}")

