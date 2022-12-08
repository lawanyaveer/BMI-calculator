#100 days python bootcamp
# 3rd day
# BMI calculator

height = float(input("what is your height in m :"))
weight = float(input("what is your weight in kg :"))
bmi = weight/(height**2)
print("your bmi is",bmi)
bmi = float(input("what is your bmi : "))
if bmi < 18.5:
    print(f"your bmi is{bmi},you're under weight")
elif bmi < 25:
        print(f"your bmi is{bmi},you're normal weight")
elif bmi < 30:
        print(f"your bmi is{bmi},you're over weight")
elif bmi <35:
        print(f"your bmi is{bmi},you're obese")
else:
    print(f"your bmi is{bmi},clinically obese")
print(round(bmi,2))