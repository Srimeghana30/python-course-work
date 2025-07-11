product_name = "Laptop"
price = 45000
in_stock = True
print(product_name, price, in_stock)

a, b, c = 10, 20, 30 #assigning values to multiple variables in a single line.
print(a, b, c) # Output: 10 20 30

x = y = z = 100 #assigning the same value to multiple variables
print(x, y, z) # Output: 100 100 100

x = 5
x = 10 #variable’s value can be updated or reassigned at any point
print(x) # Output: 10
  
a, b = 5, 10
a, b = b, a #swapping values of two variables without using a temporary variable
print(a, b) # Output: 10 5

x = 100
del x #del keyword to delete a variable
# print(x) # Raises: NameError: name 'x' is not defined