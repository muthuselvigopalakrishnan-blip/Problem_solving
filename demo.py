m=float(input("Enter the number:"))
n=float(input("Enter the number:"))
if (m+n)%2==0:
    print("Odd")
else:
    print("Even")


n=int(input("Enter the 2-digit number:"))
a=(n//10)
b=(n%10)
c=(a*b)
d=(a+b)
if (c+d)==n:
 print ("Great")
else:
    print("Not great")

customer_type = input("Enter your type (Residential / Commercial:)")
unit = int(input("Enter unit:"))
bill=0
if customer_type== "Residential":
    if unit<=100:
        bill = unit*3
    elif unit >100 and unit <=200:
        bill = unit *5
    elif unit >200:
        bill = unit*7
elif customer_type=="Commercial":
    if unit <=100:
        bill = unit*5
    elif unit >100 and unit <=200:
        bill = unit*7
    elif unit >200:
        bill = unit*10
print("your bill is",bill)

distance =float(input("Enter your traveled km:"))
fare = 0
if distance <=5:
    fare = distance*10
elif distance >5  and distance <=15:
    fare = distance * 8
else:
    fare = distance *6
print("your ola fare:",fare)

X = int(input("Enter a number1:"))
Y = int(input("Enter a number2:"))
Z = int(input("Enter a number3:"))
if X==Y==Z:
    print("Equilateral ")
elif X!=Y and Y!=Z and Z!=X:
    print("Scalene")
elif X==Y or Y==Z or Z==X:
    print("Isosceles")
else:
    print("Not a valid triangle")

a = int(input("Enter a number:"))
if a%3==0 and a%5==0:
    print("fizzbuzz")
elif a%3==0:
    print("fizz")
elif a%5==0:
    print("buzz")
else:
    print(a)



a = input("Select your path(Science/Commerce/Arts:)")
match a :
    case "Science":
       b = input ("Select your path(Medical/Engineering)")
       match b:
           case "Medical":
               print("Chosen path:Science → Medical")
           case "Enginerring":
               print("Chosen path:Science → Engineering")
           case _:
               print("not Science path")
    case "Commerce":
        c = input("Select your path(CA/B Com)")
        match c:
            case "CA":
                print("Chosen path:Commerce→ CA")
            case "B Com":
                print("Chosen path:Commerce→ B Com")
            case _:
                print("not Commerce path")
    case "Arts":
        d = input("Select your path(History/Literature)")
        match d:
            case "History":
                print("Chosen path:Arts→ History")
            case "Literature":
                print("Chosen path:Arts→ Literature")


time = int(input("enter your time (24 hours):"))
if 9<time and time<12:
    print("Morning Show")
elif 12<= time and time <16:
    print("Matinee show")
elif 16<= time and time<20:
    print("Evening Show")
else:
    print("night Show")


km = float(input("Enter value in kilometers: "))
choice = input("Enter your choice (1/2/3/4): ")
match choice:
    case "1":
        meters = km * 1000
        print(f"{km} kilometers = {meters} meters")
    case "2":
        centimeters = km * 100000
        print(f"{km} kilometers = {centimeters} centimeters")
    case "3":
        millimeters = km * 1_000_000
        print(f"{km} kilometers = {millimeters} millimeters")
    case "4":
        miles = km * 0.621371
        print(f"{km} kilometers = {miles:.4f} miles")
    case _:
        print("Invalid Conversion")