
stars = []
def rate_service():
    """Gives people 0 to 10 rating bar"""
    print(f"How much did you like our app from 0 to 10?\n")
    for x in range(1,11):
        print(f"{x:>3} - {'*' * x}")
    rating = int(input(f"\n'BUTTON IMITATING'(enter a number): "))
    if rating not in range(1, 11):
        print(f"\nPlease enter a number from 0 to 10")
        rate_service()
    elif rating == '':
        print(f"\nPlease enter a number from 0 to 10")
        rate_service()
    else:
        print("Thanks for your opinion!")
        return rating





