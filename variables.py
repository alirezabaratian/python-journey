name = "Alireza"
age = 27

print(name)
print(age)

# Python automatically determines the type of each value.
name = "Alireza"
age = 27
height = 1.89
is_engineer = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_engineer))

# 💡 Important Python Principle
# Python is dynamically typed.
# That means you don't need to declare a variable's type explicitly:
age = 27
age = "twenty-seven"  # Now age is a string
# Both assignments are valid.
# However, the type of age changes between assignments, which can affect how your code behaves.
