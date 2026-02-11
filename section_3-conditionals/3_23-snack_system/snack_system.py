snack = input("Enter your preferred snack: ").lower()

print(f"User said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
     print("Sorry, we only serve cookies or samosa with tea")
