var = str(input("Please enter a number, letter or space: "))

if var .isdigit():
    print (" have chosen a Digit.")
elif var .isalpha():
    print("You have entered a letter")
elif var .isspace():
    print("You have selected a space")
else:
    print("input not recognised, please pick one of the available options:")
    var = str(input("Please enter a number, letter or space: "))