password = input("Password: ")
special_chars = "!@#$%^&*"
if len(password) >= 8 and any(char in special_chars for char in password):
    print("Password is strong")
else:
    print("Password is not strong")