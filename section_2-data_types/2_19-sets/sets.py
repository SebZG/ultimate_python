essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"All spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
