import sqlite3


def delete_category_and_incomes(category_id):
    confirmation = input(
        "Are you sure you want to delete this category and all its incomes? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        with sqlite3.connect('econome.db') as conn:
            cursor = conn.cursor()
            # Delete all incomes associated with the category
            cursor.execute(
                "DELETE FROM Income WHERE CategoryID = ?", (category_id,))
            # Delete the category itself
            cursor.execute(
                "DELETE FROM Categories WHERE CategoryID = ?", (category_id,))
            conn.commit()
        print(
            "\033[1;92mCategory and all related incomes deleted successfully.\033[0m\n")
    else:
        print("\033[1;93mCategory deletion cancelled.\033[0m")
