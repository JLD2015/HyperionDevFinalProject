import sqlite3
from functions.get_valid_amount import get_valid_amount
from functions.calculate_available_budget import calculate_available_budget


def set_budget_for_category():
    print(
        "\n\033[1;96m<========== Set Budget for a Category ==========>\033[0m\n")

    conn = sqlite3.connect('econome.db')

    # Calculate and display available budget for the past month
    available_budget_month = calculate_available_budget(conn, 30)
    print(
        f"\033[1;93mYour available budget for the past month: \033[1;97m{available_budget_month:.2f}\033[0m")

    # Calculate and display available budget for the past year
    available_budget_year = calculate_available_budget(conn, 365)
    print(
        f"\033[1;93mYour available budget for the past year: \033[1;97m{available_budget_year:.2f}\033[0m\n")

    # Fetch and display available expense categories
    cursor = conn.cursor()
    cursor.execute(
        "SELECT CategoryID, Name FROM Categories WHERE Type = 'Expense'")
    categories = cursor.fetchall()

    # If there are no expense categories
    if not categories:
        print("\033[1;91mNo expense categories available.\033[0m\n")
        conn.close()
        return

    # Display categories
    print("\033[1;93mAvailable Expense Categories:\033[0m")
    for category in categories:
        print(f"\033[1;94m{category[0]}: \033[1;97m{category[1]}\033[0m")

    # Prompt the user to choose a category
    category_id = None
    while category_id is None:
        try:
            category_input = int(
                input("\n\033[1;96mChoose a category ID: \033[0m"))
            if any(category[0] == category_input for category in categories):
                category_id = category_input
            else:
                print("\033[1;91mInvalid Category ID. Please try again.\033[0m")
        except ValueError:
            print("\033[1;91mInvalid input. Please enter a valid number.\033[0m")

    # Enter Budget Amount
    budget_amount = get_valid_amount("\nEnter the budget amount: ")

    # Enter Budget Period
    budget_period = input(
        "\nEnter the budget period (e.g., Monthly, Annually): ").strip()

    # Insert or Update Budget
    cursor.execute(
        "SELECT Amount FROM Budgets WHERE CategoryID = ?", (category_id,))
    existing_budget = cursor.fetchone()

    if existing_budget:
        cursor.execute(
            "UPDATE Budgets SET Amount = ?, Period = ? WHERE CategoryID = ?", (budget_amount, budget_period, category_id))
        print("\n\033[1;92mBudget Updated Successfully!\033[0m\n")
    else:
        cursor.execute(
            "INSERT INTO Budgets (CategoryID, Amount, Period) VALUES (?, ?, ?)", (category_id, budget_amount, budget_period))
        print("\n\033[1;92mNew Budget Set Successfully!\033[0m\n")

    # Commit changes and close the database connection
    conn.commit()
    conn.close()
