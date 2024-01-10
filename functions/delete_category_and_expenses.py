import sqlite3


def delete_category_and_expenses(category_id):
    confirmation = input(
        "Are you sure you want to delete this category and all its expenses? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        with sqlite3.connect('econome.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Expenses WHERE CategoryID = ?", (category_id,))
            cursor.execute(
                "DELETE FROM Categories WHERE CategoryID = ?", (category_id,))
            conn.commit()
        print(
            "\033[1;92mCategory and all related expenses deleted successfully.\033[0m\n")
    else:
        print("\033[1;93mCategory deletion cancelled.\033[0m")
