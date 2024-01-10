import sqlite3


def delete_income(income_id):
    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Income WHERE IncomeID = ?", (income_id,))
        conn.commit()
    print("\n\033[1;92mIncome deleted successfully.\033[0m\n")
