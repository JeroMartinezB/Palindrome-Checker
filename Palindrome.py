# Joshua Clemas, Jeronimo Martinez Barragan
# Lecture Feb 6th
# Pair programming exercise - Palindrome Number Checker

print("Palindrome checker:")
while True:
    # User input
    user_input = input("Enter your sentence or press q to quit: ")
    if user_input.lower() == 'q':
        break

    # Use lists to compare
    original = list(user_input)
    reversed = original[::-1]

    # Compare
    if original == reversed:
        print("Palindrome!")
    else:
        print("Not a palindrome")
