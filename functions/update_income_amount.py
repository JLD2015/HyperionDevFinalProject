import sqlite3
from functions.get_valid_amount import get_valid_amount


def update_income_amount(income_id):
    new_amount = get_valid_amount("Enter the new income amount: ")
    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Income SET Amount = ? WHERE IncomeID = ?", (new_amount, income_id))
        conn.commit()
    print("\n\033[1;92mIncome amount updated successfully.\033[0m\n")
