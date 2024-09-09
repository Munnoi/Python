# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(k or L): ")


if unit == 'K':
  weight = weight * 2.205
  print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == 'L':
  weight = weight / 2.205
  print(f"Your weight is {round(weight, 2)} {unit}")
else:
  print(f"{unit} was not valid!")
