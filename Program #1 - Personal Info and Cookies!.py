#the goal of this program is to get user personal information and print it.
#It is also to compute the number of cookies that the user inputs based upon
#the formula (1.5 cup sugars+1 cup butter+2.75 cup flour = 48 cookies)
#
#Define our variables
#Get personal info from user
name = input("What is your name? ")
address = input("Enter your address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zipcode = input("Enter your zipcode: ")
phonenumber = input("Enter your phone number: ")
major = input("Enter your major: ")

#Get the number of cookies that the user want to bake
cookies = int(input ("Enter the number of cookies you would like to bake: "))
sugar = 1.5
butter = 1
flour = 2.75
scale = cookies / 48
new_sugar = (sugar * scale)
new_butter = (butter * scale)
new_flour = (flour * scale)

#cookieingredients = ((sugar + butter + flour)/48)

#This is the output section of the program
print("Name is:", name)
print("Address is:", address, city, state, zipcode)
print("Phone Number is:", phonenumber)
print("Major is:", major)
print("How many cookies would you like to bake?", cookies)
print("Ingredients for the cookies include:", f"{new_sugar:.2f}","cup(s) of sugar,", f"{new_butter:.2f}", "cup(s) of butter, and", f"{new_flour:.2f}", "cup(s) of flour")

