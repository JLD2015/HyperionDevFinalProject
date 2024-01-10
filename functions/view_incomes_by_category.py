import sqlite3
from functions.delete_category_and_incomes import delete_category_and_incomes


def view_incomes_by_category():
    print("\n\033[1;96m<========== View Incomes by Category ==========>\033[0m\n")

    # Connect to the database
    conn = sqlite3.connect('econome.db')
    cursor = conn.cursor()

    # Fetch and display available income categories
    cursor.execute(
        "SELECT CategoryID, Name FROM Categories WHERE Type = 'Income'")
    categories = cursor.fetchall()

    if not categories:
        print("\033[1;91mNo income categories available.\033[0m\n")
        conn.close()
        return

    # Display categories with color
    print("\033[1;93mAvailable Categories:\033[0m")
    for category in categories:
        print(f"\033[1;94m{category[0]}: \033[1;97m{category[1]}\033[0m")

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

    cursor.execute('''
        SELECT IncomeID, Amount, Date, Description
        FROM Income
        WHERE CategoryID = ?
        ORDER BY Date ASC
    ''', (category_id,))
    incomes = cursor.fetchall()

    if incomes:
        # Color coded header
        print("\n\033[1;93m{:<10} {:<10} {:<15} {:<30}\033[0m".format(
            'ID', 'Amount', 'Date', 'Description'))
        print("\033[1;95m" + "-" * 65 + "\033[0m")

        # Display each income in color
        for income in incomes:
            print(
                "\033[1;97m{:<10} {:<10.2f} {:<15} {:<30}\033[0m".format(*income))
        print('\n')

    # Offer deletion option whether or not there are incomes in the category
    delete_option = input(
        "\nDo you want to delete this category and all its incomes? (yes/no): ").strip().lower()
    if delete_option == 'yes':
        delete_category_and_incomes(category_id)  # Function to be implemented
    else:
        print("\n\033[1;92mCategory retained.\033[0m\n")

    # Close the database connection
    conn.close()
