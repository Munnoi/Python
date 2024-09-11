foods = [] 
prices = []
total = 0

while True:
  food = input("Enter a food to buy (q to quit): ").lower()
  if food == 'q':
    break
  else:
    price = float(input(f"Enter the prie of {food}: "))
    foods.append(food)
    prices.append(price)

print("----- Your Cart -----")

for idx, food in enumerate(foods):
  print(f"{idx+1}.{food}")
print()

for price in prices:
  total += price

print(f"Your total is: {total:.2f}")