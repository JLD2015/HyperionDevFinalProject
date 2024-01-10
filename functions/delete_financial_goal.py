import sqlite3


def delete_financial_goal(goal_id):
    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM FinancialGoals WHERE GoalID = ?", (goal_id,))
        conn.commit()
    print("\n\033[1;92mFinancial goal deleted successfully.\033[0m\n")
