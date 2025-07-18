import math

# Input from user
A = int(input("Enter a number: "))

# Square root
if A < 0:
    print("Square root is not defined for negative numbers.")
else:
    sqrt_value = math.sqrt(A)
    print("The square root is:", sqrt_value)

# Natural log
if A <= 0:
    print("Natural logarithm is not defined for zero or negative numbers.")
else:
    natural_log = math.log(A)
    print(f"The natural logarithm of {A} is:", natural_log)

# Sin value (assuming input in degrees)
sin_value = math.sin(math.radians(A))
print(f"The value of sin({A} degrees) is:", sin_value)
