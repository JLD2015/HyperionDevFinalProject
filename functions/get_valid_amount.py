def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:  # Allows zero and positive numbers
                return amount
            else:
                print("\033[1;91mAmount must be non-negative.\033[0m")
        except ValueError:
            print("\033[1;91mPlease enter a valid number.\033[0m")
