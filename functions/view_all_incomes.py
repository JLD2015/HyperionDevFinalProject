import sqlite3
from functions.update_income_amount import update_income_amount  
from functions.delete_income import delete_income  

def view_all_incomes():
    print("\n\033[1;96m<========== View All Incomes ==========>\033[0m\n")

    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT IncomeID, c.Name as Category, Amount, Date, Description
            FROM Income i
            JOIN Categories c ON i.CategoryID = c.CategoryID
            ORDER BY i.Date ASC
        ''')
        incomes = cursor.fetchall()

    if incomes:
        print("\033[1;93m{:<10} {:<20} {:<10} {:<15} {:<30}\033[0m".format(
            'ID', 'Category', 'Amount', 'Date', 'Description'))
        print("\033[1;95m" + "-" * 85 + "\033[0m")
        for income in incomes:
            print(
                "\033[1;97m{:<10} {:<20} {:<10.2f} {:<15} {:<30}\033[0m".format(*income))
        print("\n")

        while True:
            try:
                user_action = input(
                    "\033[1;93mEnter the ID of an income to modify or 'q' to go back: \033[0m").strip()
                if user_action.lower() == 'q':
                    break
                income_id = int(user_action)
                if any(income[0] == income_id for income in incomes):
                    choice = input(
                        "\nEnter 'u' to update the amount, 'd' to delete the income, or 'q' to cancel: ").lower()
                    if choice == 'u':
                        update_income_amount(income_id)  # Function to be implemented
                        break
                    elif choice == 'd':
                        delete_income(income_id)  # Function to be implemented
                        break
                    elif choice == 'q':
                        break
                    else:
                        print("\033[1;91mInvalid option. Please try again.\033[0m")
                else:
                    print("\033[1;91mInvalid Income ID. Please try again.\033[0m")
            except ValueError:
                print("\033[1;91mPlease enter a valid number.\033[0m")
    else:
        print("\033[1;91mNo incomes recorded yet.\033[0m\n")
