cm = float(input("Height:"))
kg = float(input("Weight:"))
m = cm / 100
bmi = kg / (m * m)
if 0 < bmi < 16:
    print("Severely underweight")
elif 0 < bmi <= 18.5:
    print("Underweight")
elif 0 < bmi <= 25:
    print("Normal")
elif 0 < bmi <= 30:
    print("Overweight")
elif bmi > 30:
    print("Obese")
else:
    print("0 is not an appropriate number")