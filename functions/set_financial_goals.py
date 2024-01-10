import sqlite3
from functions.get_valid_amount import get_valid_amount
from functions.validate_date import validate_date
import datetime


def set_financial_goals():
    print("\n\033[1;96m<========== Set Financial Goals ==========>\033[0m\n")

    # Get goal description
    description = input(
        "\033[1;93mEnter a description for your financial goal: \033[0m").strip()

    # Get target amount
    target_amount = get_valid_amount(
        "\033[1;93mEnter your target amount: \033[0m")

    # Get current amount
    current_amount = get_valid_amount(
        "\033[1;93mEnter your current amount towards this goal: \033[0m")

    # Get deadline
    deadline_input = input(
        "\033[1;93mEnter the deadline for your goal (YYYY-MM-DD) or press Enter for today's date: \033[0m").strip()

    # Use today's date if the input is empty
    deadline = deadline_input if deadline_input else datetime.datetime.now().strftime('%Y-%m-%d')

    # Validate the date input
    while not validate_date(deadline):
        deadline = input(
            "\033[1;91mInvalid date. Please enter the date in YYYY-MM-DD format or press Enter for today's date: \033[0m").strip()
        if not deadline:
            deadline = datetime.datetime.now().strftime('%Y-%m-%d')
            break

    # Connect to the database
    conn = sqlite3.connect('econome.db')
    cursor = conn.cursor()

    # Insert the new goal into the FinancialGoals table
    cursor.execute("INSERT INTO FinancialGoals (Description, TargetAmount, CurrentAmount, Deadline) VALUES (?, ?, ?, ?)",
                   (description, target_amount, current_amount, deadline))
    conn.commit()

    print("\n\033[1;92mFinancial Goal Set Successfully!\033[0m\n"
          f"\033[1;94mDescription: \033[1;97m{description}\033[0m\n"
          f"\033[1;94mTarget Amount: \033[1;97m{target_amount}\033[0m\n"
          f"\033[1;94mCurrent Amount: \033[1;97m{current_amount}\033[0m\n"
          f"\033[1;94mDeadline: \033[1;97m{deadline}\033[0m\n")

    # Close the database connection
    conn.close()
