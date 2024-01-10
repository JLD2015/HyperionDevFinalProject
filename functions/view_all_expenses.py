import sqlite3
from functions.update_expense_amount import update_expense_amount
from functions.delete_expense import delete_expense


def view_all_expenses():
    print("\n\033[1;96m<========== View All Expenses ==========>\033[0m\n")

    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT ExpenseID, c.Name as Category, Amount, Date, Description
            FROM Expenses e
            JOIN Categories c ON e.CategoryID = c.CategoryID
            ORDER BY e.Date ASC
        ''')
        expenses = cursor.fetchall()

    if expenses:
        print("\033[1;93m{:<10} {:<20} {:<10} {:<15} {:<30}\033[0m".format(
            'ID', 'Category', 'Amount', 'Date', 'Description'))
        print("\033[1;95m" + "-" * 85 + "\033[0m")
        for expense in expenses:
            print(
                "\033[1;97m{:<10} {:<20} {:<10.2f} {:<15} {:<30}\033[0m".format(*expense))
        print("\n")

        while True:
            try:
                user_action = input(
                    "\033[1;93mEnter the ID of an expense to modify or 'q' to go back: \033[0m").strip()
                if user_action.lower() == 'q':
                    break
                expense_id = int(user_action)
                if any(expense[0] == expense_id for expense in expenses):
                    choice = input(
                        "\nEnter 'u' to update the amount, 'd' to delete the expense, or 'q' to cancel: ").lower()
                    if choice == 'u':
                        update_expense_amount(expense_id)
                        break
                    elif choice == 'd':
                        delete_expense(expense_id)
                        break
                    elif choice == 'q':
                        break
                    else:
                        print(
                            "\033[1;91mInvalid option. Please try again.\033[0m")
                else:
                    print(
                        "\033[1;91mInvalid Expense ID. Please try again.\033[0m")
            except ValueError:
                print("\033[1;91mPlease enter a valid number.\033[0m")
    else:
        print("\033[1;91mNo expenses recorded yet.\033[0m\n")
