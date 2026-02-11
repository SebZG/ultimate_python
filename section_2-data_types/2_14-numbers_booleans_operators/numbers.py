import sys

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")


remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving} litres")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"leftover Cardamom pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength**scale_factor
print(f"Sacaled flavor strength {powerful_flavor}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves: {total_tea_leaves_harvested}")

ideal_temp = 95.5
current_temp = 95.499999

print(f"Ideal temp {ideal_temp}")
print(f"Ideal temp {current_temp}")
print(f"Difference temp {ideal_temp - current_temp}")
print(sys.float_info)
