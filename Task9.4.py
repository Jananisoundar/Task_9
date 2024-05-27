import re

# a. Validate Email Address
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# b. Validate Mobile Number of Bangladesh
def is_valid_bangladesh_mobile(number):
    mobile_regex = r'^(\+8801|8801|01)[3-9]\d{8}$'
    return re.match(mobile_regex, number) is not None

# c. Validate Telephone Number of USA
def is_valid_usa_telephone(number):
    telephone_regex = r'^\+1-\d{3}-\d{3}-\d{4}$'
    return re.match(telephone_regex, number) is not None

# d. Validate 16 Character Alpha-numeric Password
def is_valid_password(password):
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return re.match(password_regex, password) is not None

# Example usage:
emails = ["example@example.com", "invalid-email"]
bangladesh_numbers = ["+8801712345678", "01912345678", "8801912345678", "0112345678"]
usa_telephones = ["+1-123-456-7890", "123-456-7890"]
passwords = ["Aa1@123456789012", "invalidpassword", "Aa1@Aa1@Aa1@Aa1@"]

print("Email Validation:")
for email in emails:
    print(f"{email}: {is_valid_email(email)}")

print("\nBangladesh Mobile Number Validation:")
for number in bangladesh_numbers:
    print(f"{number}: {is_valid_bangladesh_mobile(number)}")

print("\nUSA Telephone Number Validation:")
for number in usa_telephones:
    print(f"{number}: {is_valid_usa_telephone(number)}")

print("\nPassword Validation:")
for password in passwords:
    print(f"{password}: {is_valid_password(password)}")
