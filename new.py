sentence="Rajarajeshwari-is-my-frnd"
substring=sentence.split('-')
for word in substring:
    print(word)


str1 = "Divagar"
reversed_str = str1[::-1]
print(reversed_str)

str1 = "Muthuselvi"
for i in range(len(str1)-1, -1, -1):
    reversed_str += str1[i]
print(reversed_str)



password = input("Password: ")
special_chars = "!@#$%^&*"
if len(password) >= 8 and any(char in special_chars for char in password):
    print("Password is strong")
else:
    print("Password is not strong")


text = "I like dog "
no_spaces = text.replace(" ", "")
print(no_spaces)

text = "I like dog"
text = text.lower()
vowels = "aeiou"
consonant_count = 0
for char in text:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print("Number of consonants:", consonant_count)

