chai_type = "Ginger chai"
customer_name = "seb"

print(f"Order for {customer_name}: {chai_type}")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8:2]}")
print(f"Last word: {chai_description[12:]}")
print(f"Reverse word: {chai_description[::-1]}")

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(f"None encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
dencoded_label = encoded_label.decode("utf-8")
print(f"Dencoded label: {dencoded_label}")
