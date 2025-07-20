PhoneNum = {
    "0500167148" : "Majed",
    "2222222222" : "Amal",
     "1111111111" : "Fahad",
    "3333333333" : "Rawan"}

number = input("Enter a number: ")

if len(number) != 10:
    print("Invalid Number")
elif number in PhoneNum:
    print("Oener Number is ",PhoneNum[number])
else:
    print("Sorry, This Number is not Found")