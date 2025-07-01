name = input("Enter your name: ")
print(f"Hello, {name}!")


# prompt that includes math, as input is always a string 
size_input = input("How big is your house? (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.764
# .2f formats the number to 2 decimal places 
print(f"Your House is approx. {square_meters:.2f} square meters.")