str1 = "Divagar"
reversed_str = str1[::-1]
print(reversed_str)

str1 = "Muthuselvi"
for i in range(len(str1)-1, -1, -1):
    reversed_str += str1[i]
print(reversed_str)
