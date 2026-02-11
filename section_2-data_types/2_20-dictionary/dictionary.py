chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"chai_order: {chai_order}")

chai_recipe = {}
chai_recipe["Base"] = "Black Tea"
chai_recipe["Liquid"] = "Milk"
print(f"Recipe Base: {chai_recipe['Base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["Liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {"sugar" in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"Cardamom": "crushed", "Ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("note", "NO NOTE")
print(f"Chai size is: {customer_note}")
