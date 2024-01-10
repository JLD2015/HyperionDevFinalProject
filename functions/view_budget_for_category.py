import sqlite3


def view_budget_for_category():
    print(
        "\n\033[1;96m<========== View Budget for a Category ==========>\033[0m\n")

    # Connect to the database
    conn = sqlite3.connect('econome.db')
    cursor = conn.cursor()

    # Fetch and display available expense categories
    cursor.execute(
        "SELECT CategoryID, Name FROM Categories WHERE Type = 'Expense'")
    categories = cursor.fetchall()

    if not categories:
        print("\033[1;91mNo expense categories available.\033[0m\n")
        conn.close()
        return

    # Display categories with color
    print("\033[1;93mAvailable Expense Categories:\033[0m")
    for category in categories:
        print(f"\033[1;94mID {category[0]}: \033[1;97m{category[1]}\033[0m")

    print("\n----------------------------------------\n")

    # Prompt the user to choose a category
    category_id = None
    while category_id is None:
        try:
            category_input = int(
                input("\033[1;96mChoose a category ID: \033[0m"))
            if any(category[0] == category_input for category in categories):
                category_id = category_input
            else:
                print("\033[1;91mInvalid Category ID. Please try again.\033[0m")
        except ValueError:
            print("\033[1;91mInvalid input. Please enter a valid number.\033[0m")

    # Fetch the budget for the selected category
    cursor.execute(
        "SELECT Amount, Period FROM Budgets WHERE CategoryID = ?", (category_id,))
    budget = cursor.fetchone()

    # Display the budget information
    if budget:
        amount, period = budget
        print(f"\n\033[1;93mBudget Details for Selected Category:\033[0m")
        print(f"  \033[1;94mAmount: \033[1;97m{amount}\033[0m")
        print(f"  \033[1;94mPeriod: \033[1;97m{period}\033[0m\n")
    else:
        print(f"\n\033[1;91mNo budget set for this category.\033[0m\n")

    # Close the database connection
    conn.close()
