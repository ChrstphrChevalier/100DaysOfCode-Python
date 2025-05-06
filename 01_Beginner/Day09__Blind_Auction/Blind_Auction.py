import art

print(art.logo)
print("Welcome to the secret auction program.")

secret_auction = {}

while True:
    while True:
        name = input("What is your name ?: ")
        if name.isalpha():
            break
        else:
            print("Invalid input! Please enter a name that contains only letters.")


    while True:
        try:
            bid = input("What's your bid ?: $")
            bid = int(bid)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for your bid.")

    secret_auction[name] = bid
    other_bidders = input("Are there any other bidders ? Type 'yes or 'no': ")
    if other_bidders == 'no':
        best_bid = ("", 0)
        for key, value in secret_auction.items():
            if value > best_bid[1]:
                best_bid = (key, value)
        print("\n" * 40)
        print(f"The winner is {best_bid[0]} with a bid of ${best_bid[1]}")
        break
    elif other_bidders == 'yes':
        print("\n" * 40)
    elif other_bidders != 'yes':
        print("Secret auction cancelled.")