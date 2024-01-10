import sqlite3


def delete_expense(expense_id):
    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Expenses WHERE ExpenseID = ?", (expense_id,))
        conn.commit()
    print("\n\033[1;92mExpense deleted successfully.\033[0m\n")
