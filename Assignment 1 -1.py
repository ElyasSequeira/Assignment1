#variables
Shirtprice = float(9.99)
HST = float(1.13)
colourChoose = input(str("hello, welcome to Abby's Merchandizing! Ready to order? start by typing which colour of shirt you would like: "))
cosel = str(colourChoose)
print("you have chosen a " + colourChoose + " coloured shirt.")
shirtstyle = input(str("Now select a style of shirt! (Polo/T-shirt) "))
print("you have selected a " + shirtstyle + " styled shirt.")
print("please select the amount of shirts you would like: ")
quant = int(input())
atax = str(quant * 1.13)
print("Selected quantity: " + str(quant))
check= str(input("ready to checkout? 'YES/NO': "))
if check == (str("YES")):
    print("your order:")
    print(str(quant) + " " + colourChoose + " " + shirtstyle + "           " + "    %.2f " % float(str((float(Shirtprice * quant)))))
    quantfin = Shirtprice * quant
    total = float(atax) + quantfin
    print("tax:                       %.2f "  % float(atax))
    print("Total ===================  %.2f" % total)
    print("Thank you for shopping!")
else:
    print("please come back soon!")

#DONT GO BACK FURTHER