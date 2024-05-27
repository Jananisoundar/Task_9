# write a python code using lambda function to check every element of a list is an integer or string?
data = [10, '501', 22, 'hello', 100, 'world', 87, 351]

# Function to check if an element is an integer
is_integer = lambda x: isinstance(x, int)

# Function to check if an element is a string
is_string = lambda x: isinstance(x, str)

# Apply the lambda functions to each element in the list
int_check = list(map(is_integer, data))
str_check = list(map(is_string, data))

print(f"Check if each element is an integer: {int_check}")
print(f"Check if each element is a string: {str_check}")
