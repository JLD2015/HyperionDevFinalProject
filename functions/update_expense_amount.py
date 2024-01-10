import sqlite3
from functions.get_valid_amount import get_valid_amount
# Import the budget check function
from functions.check_budget_overrun import check_budget_overrun


def update_expense_amount(expense_id):
    new_amount = get_valid_amount("Enter the new expense amount: ")

    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()

        # First, find the category ID for this expense
        cursor.execute(
            "SELECT CategoryID FROM Expenses WHERE ExpenseID = ?", (expense_id,))
        category_id = cursor.fetchone()[0]

        # Update the expense amount
        cursor.execute(
            "UPDATE Expenses SET Amount = ? WHERE ExpenseID = ?", (new_amount, expense_id))
        conn.commit()

        # Check for budget overrun
        check_budget_overrun(category_id)

    print("\n\033[1;92mExpense amount updated successfully.\033[0m\n")
