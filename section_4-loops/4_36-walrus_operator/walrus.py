# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisable, remainder is {remainder}")

value = 13

if remainder := value % 5:
    print(f"Not divisable, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print("Size is unavailable")


flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavours: ", flavours)

while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"You choose {flavour} chai")
