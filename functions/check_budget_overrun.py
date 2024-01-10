import sqlite3


def check_budget_overrun(category_id):
    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()

        # Get the total expenses for the category
        cursor.execute(
            "SELECT SUM(Amount) FROM Expenses WHERE CategoryID = ?", (category_id,))
        total_expenses = cursor.fetchone()[0] or 0

        # Get the budget limit for the category
        cursor.execute(
            "SELECT Amount FROM Budgets WHERE CategoryID = ?", (category_id,))
        budget = cursor.fetchone()

        if budget and total_expenses > budget[0]:
            print(
                "\n\033[1;91mWarning: You have exceeded your budget for this category!\033[0m\n")
            print(
                f"\033[1;93mTotal Expenses: {total_expenses} | Budget Limit: {budget[0]}\033[0m\n")
