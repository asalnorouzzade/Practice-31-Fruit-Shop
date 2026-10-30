# https://github.com/asalnorouzzade/Practice-31-Fruit-Shop.git
def shopping_list(**fruits):
    count = len(fruits)
    total_cost = sum(fruits.values())
    most_expensive = max(fruits, key=fruits.get)
    cheapest = min(fruits, key=fruits.get)
    print(f"You have {count} fruits in your shopping list")
    print(f"The total cost of the shopping list is {total_cost}")
    print(f"The most expensive fruit is {most_expensive} with the price of {fruits[most_expensive]}")
    print(f"The cheapest fruit is {cheapest} with the price of {fruits[cheapest]}")

shopping_dictionary = {}
while True:
    line = input()
    if line == "finish":
        break
    parts = line.split()
    name = parts[0]
    price = int(parts[1]) 
    shopping_dictionary[name] = price
shopping_list(**shopping_dictionary)
