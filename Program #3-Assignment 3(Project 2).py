item1 = input("Enter the first item: ")
price1 = float(input("Enter the price of the first item: "))
item2 = input("Enter the second item: ")
price2 = float(input("Enter the price of the second item: "))
item3 = input("Enter the third item: ")
price3 = float(input("Enter the price of the third item: "))
item4 = input("Enter the fourth item: ")
price4 = float(input("Enter the price of the fourth item: "))
item5 = input("Enter the fifth item: ")
price5 = float(input("Enter the price of the fifth item: "))
item6 = input("Enter the sixth item: ")
price6 = float(input("Enter the price of the sixth item: "))


print("\nHere is the menu!")
print("1-",item1,":", f"${price1:.2f}")
print("2-",item2,":", f"${price2:.2f}")
print("3-",item3,":", f"${price3:.2f}")
print("4-",item4,":", f"${price4:.2f}")
print("5-",item5,":", f"${price5:.2f}")
print("6-",item6,":", f"${price6:.2f}")

sentinel = "quit"
while(search := input("\nEnter item to search(or type quit to exit): ")):
    if search == sentinel:
        print("Thanks for stopping by!")
        break
    elif search == item1:
        print(f"{item1} is on the menu for ${price1:.2f}")
    elif search == item2:
        print(f"{item2} is on the menu for ${price2:.2f}")
    elif search == item3:
        print(f"{item3} is on the menu for ${price3:.2f}")
    elif search == item4:
        print(f"{item4} is on the menu for ${price4:.2f}")
    elif search == item5:
        print(f"{item5} is on the menu for ${price5:.2f}")
    elif search == item6:
        print(f"{item6} is on the menu for ${price6:.2f}")
    else:
        print(f"{search} is not on the menu. Enter another item.")
        continue
