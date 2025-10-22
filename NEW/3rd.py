text = "I like dog"
text = text.lower()
vowels = "aeiou"
consonant_count = 0
for char in text:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print("Number of consonants:", consonant_count)