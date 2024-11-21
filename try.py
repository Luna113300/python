weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres: "))

if weight == 0 or height == 0:
    print(f'Your weight is: {weight}kg.')
    print(f'Your height is: {height}m.')
    print("Enter a value greater than 0. Try Again...")

elif  weight < 0 or height < 0:
    print("Error: Enter a positive value. Try Again...")

else:
 bmi = weight / height ** 2

if bmi < 18.5:
    print(f'Your BMI is:{bmi}. (under weight)')

elif 18.5 <= bmi < 25:
    print(f'Your BMI is:{bmi}. (Normal weight)')

elif 25 <= bmi < 30:
    print(f'Your BMI is:{bmi}. (over weight)')

else:
    print(f'your BMI is: {bmi}. (obesity)')