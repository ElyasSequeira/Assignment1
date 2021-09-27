alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbchos = input(str("welcome, please input a value that numarlically represents the letter you have chosen(*0-25 for lowercase*26-51 for uppercase*): "))
numbF = int(numbchos)
print("you have chosen '" + numbchos + "' which represents the letter: '" + (alphabet[numbF]) + "'")
output = (alphabet[numbF])
convl = (str.lower(output))
convU = (str.capitalize(output))
print("Time to Convert!")
if output == str.lower(output):
    print("The Capitolised latter of your choice is: " + convU)

else:
    print("The Capitolised latter of your choice is: " + convl)
    
