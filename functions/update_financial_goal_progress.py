import sqlite3
from functions.get_valid_amount import get_valid_amount


def update_financial_goal_progress(goal_id):
    with sqlite3.connect('econome.db') as conn:
        cursor = conn.cursor()

        # Retrieve the target amount for the goal
        cursor.execute(
            "SELECT TargetAmount FROM FinancialGoals WHERE GoalID = ?", (goal_id,))
        target_amount = cursor.fetchone()[0]

        new_amount = get_valid_amount(
            "Enter the new current amount towards this goal: ")

        # Check if the new amount exceeds the target amount
        if new_amount > target_amount:
            over_amount = new_amount - target_amount
            print(
                f"\n\033[1;91mThe current amount exceeds the target by {over_amount:.2f}.\033[0m\n")

            # Offer to adjust to 100% completion
            adjust = input(
                "Would you like to adjust the amount to reach 100% completion? (yes/no): ").strip().lower()
            if adjust == 'yes':
                new_amount = target_amount
                print(
                    "\n\033[1;92mAmount adjusted to match the target amount for 100% completion.\033[0m\n")

        # Update the current amount in the database
        cursor.execute(
            "UPDATE FinancialGoals SET CurrentAmount = ? WHERE GoalID = ?", (new_amount, goal_id))
        conn.commit()

    print("\n\033[1;92mFinancial goal progress updated successfully.\033[0m\n")
