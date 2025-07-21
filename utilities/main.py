import calculator
import string_operations

print("using calulator.py")
print("Addition: ", calculator.add(4, 2))
print("Subtracting: ",calculator.subtract(4, 2))
print("Multiplying", calculator.multiply(4, 2))
print("Dividing: ", calculator.divide(4, 2))

print("using string_operation.py")
print("Reversing string: ", string_operations.revers_string("Hello, World!"))
print("Capitalizing string: ", string_operations.capitalize_string("hello, world!"))
print("Lowercasing string: ", string_operations.lowercase_string("HELLO, WORLD!"))
print("Uppercasing string: ", string_operations.uppercase_string("hello, world!"))