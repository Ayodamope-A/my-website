while True:
    if (ratings := input('''Enter a number from 1 to 5 or "exit" to exit: ''')) == "exit":
        break

    try:
        rating = int(ratings)
        
       
        if 1 <= rating <= 5:

            if rating == 5:
                print("Ratings are excellent")
            elif rating == 4:
                print("Ratings are good")
            elif rating == 3:
                print("Ratings are average")
            elif rating == 2:
                print("Ratings are poor")
            elif rating == 1:
                print("Ratings are terrible")

        else:
            print("Invalid input. Please enter a number between 1 and 5 or 'exit'.")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5 or 'exit': ")
        continue

print("Survey Ended")

