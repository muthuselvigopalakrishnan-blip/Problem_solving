'''
n = int(input("Enter a number: "))

i = 1
while n >=i:
    print(i** 3)
    i=i+1
'''
'''starting_value=1
ending_value=5
while starting_value<+ending_value:
    print(starting_value)
    starting_value=starting_value+1'''
'''a=int(input("enter the number:"))
b=int(input("enter the value:"))
i=1
while i<=b:
    print(a)
    a=a+1
    i=i+1'''
'''a=int(inut("enter the number:"))
i=1
while i<=a:
   num=(i**2)+1
   print(num,end=" ")
   i+=1'''

'''a=int(input("Enter a number:"))
i=1
while i<=a:
    print(a)
    i=i+1'''
'''a=int(input("enter a value:"))
b=int(input("enter a value:"))
for i in range(b,a-1,-1):
    print(i)'''
'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
for i in range (2,n+2):
    print(i)'''
'''x=int(input("Enter the values:"))
if x%4==0 and x%100!=0 or x %400==0:
    print("y")
else :
     print("N")'''

'''a = int(input("Enter a number1:"))
b = int(input("Enter a number2:"))
count = 0
while a <= b:
    if a % 2 == 0:
        count =count+ a
    a =a+ 1
print(count)'''
'''a=str(input("My name is :"))
b=str(input("My age:"))
c=a+b 
print(c)'''
'''km=int(input("Enter the value:"))
if km>0 and km<=10:
    f=km*15
    print(f)
elif km>10 and km<=20:
    f=(10*15)+(km-10)*12
    print(f)
elif km>20 and km <=30:
    f=(10*15)+(20*12)+(km-30)*10
    print(f)'''
'''months=int(input("erer"))
total = 0
monthly_saving = 100
for month in range(1, months + 1):
    total += monthly_saving
    monthly_saving += 50  # increase by 50 every month
print(total)'''
'''steps=int(input("Enter the number:"))
def total_reward(steps):
    reward = (steps // 1000) * 5
    if steps>=5000:
        reward+=20
    print (reward)'''

'''def Buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
def is_run_fizz_Buzz(limit):
    for i in range(1,limit+1):
        fizz_Buzz(i)
is_run_fizz_Buzz(20)'''
'''a=[1,5,7,3,9,14,8,15]
for num in a:
  if num <50:
    print(num)'''
'''sentence="I am Iron Man "
slied_str=sentence[5:9]
print(slied_str)'''
'''sentence="I am Iron Man "
slied_str=sentence[5:]
print(slied_str)'''
'''sentence="I am Iron Man "
slied_str=sentence[:4]
print(slied_str)'''



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

