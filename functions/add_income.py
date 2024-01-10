import sqlite3
from datetime import datetime
from functions.get_or_create_category import get_or_create_category
from functions.get_valid_amount import get_valid_amount
from functions.validate_date import validate_date


def add_income():
    # Print the header for the add income section with color
    print("\n\033[1;96m<========== Add Income ==========>\033[0m\n")

    # Get the category ID for the income from the user
    category_id = get_or_create_category("Income")

    # Prompt the user to enter the amount for the income
    amount = get_valid_amount("\nEnter the income amount: ")

    # Ask the user for the date of the income
    date_input = input(
        "\nEnter the date (YYYY-MM-DD) or press Enter for today's date: ").strip()

    # Validate the date input or use today's date if the user presses Enter
    if date_input:
        while not validate_date(date_input):
            date_input = input(
                "\033[1;91mInvalid date. Please enter the date in YYYY-MM-DD format or press Enter for today's date: \033[0m").strip()
            if not date_input:
                break

    # Set the date to the user input or to today's date if the input is empty
    date = date_input if date_input else datetime.now().strftime('%Y-%m-%d')

    # Get an optional description for the income
    description = input("\nEnter a description (optional): ")

    # Connect to the database and insert the new income
    conn = sqlite3.connect('econome.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Income (CategoryID, Amount, Date, Description) VALUES (?, ?, ?, ?)",
                   (category_id, amount, date, description))
    conn.commit()

    # Fetch the name of the category for display
    cursor.execute(
        "SELECT Name FROM Categories WHERE CategoryID = ?", (category_id,))
    category_name = cursor.fetchone()[0]

    # Print a confirmation message with details of the added income
    print("\n\033[1;92mIncome Added Successfully!\033[0m\n"
          f"\033[1;94mCategory: \033[1;97m{category_name}\033[0m\n"
          f"\033[1;94mAmount: \033[1;97mR{amount:.2f}\033[0m\n"
          f"\033[1;94mDate: \033[1;97m{date}\033[0m\n"
          f"\033[1;94mDescription: \033[1;97m{description if description else 'N/A'}\033[0m\n")

    # Close the database connection
    conn.close()
