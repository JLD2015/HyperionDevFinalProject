import sqlite3
from functions.delete_financial_goal import delete_financial_goal
from functions.update_financial_goal_progress import update_financial_goal_progress


def view_financial_goals_progress():
    print("\n\033[1;96m<========== Financial Goals Progress ==========>\033[0m\n")

    # Connect to the database
    conn = sqlite3.connect('econome.db')
    cursor = conn.cursor()

    # Fetch all financial goals
    cursor.execute(
        "SELECT GoalID, Description, TargetAmount, CurrentAmount, Deadline FROM FinancialGoals")
    goals = cursor.fetchall()

    if not goals:
        print("\033[1;91mNo financial goals set yet.\033[0m\n")
        conn.close()
        return

    # Print header with color
    header = "{:<10} {:<30} {:<15} {:<15} {:<15} {:<10}".format(
        "ID", "Description", "Target Amount", "Current Amount", "Deadline", "Progress")
    print("\033[1;93m{}\033[0m".format(header))
    print("\033[1;95m" + "-" * 95 + "\033[0m")

    # Display each goal and its progress
    for goal in goals:
        goal_id, description, target_amount, current_amount, deadline = goal
        progress = (current_amount / target_amount) * \
            100 if target_amount > 0 else 0

        # Color coding the progress
        progress_color = "\033[1;92m" if progress >= 100 else "\033[1;93m" if progress >= 50 else "\033[1;91m"

        goal_line = "{:<10} {:<30} {:<15.2f} {:<15.2f} {:<15} {}{:<10.2f}%\033[0m".format(
            goal_id, description, target_amount, current_amount, deadline, progress_color, progress)
        print(goal_line)

    print("\n")  # Extra newline for better spacing

    # Interaction for updating or deleting goals
    while True:
        user_action = input(
            "\033[1;93mEnter the ID of a goal to modify or 'q' to go back: \033[0m").strip()
        if user_action.lower() == 'q':
            break

        try:
            goal_id = int(user_action)
            # Check if the goal_id exists
            if any(goal[0] == goal_id for goal in goals):
                choice = input(
                    "\nEnter 'u' to update progress, 'd' to delete the goal, or 'q' to cancel: ").lower()
                if choice == 'u':
                    update_financial_goal_progress(goal_id)
                    break
                elif choice == 'd':
                    delete_financial_goal(goal_id)
                    break
                elif choice == 'q':
                    break
                else:
                    print("\033[1;91mInvalid option. Please try again.\033[0m")
            else:
                print("\033[1;91mInvalid Goal ID. Please try again.\033[0m")
        except ValueError:
            print("\033[1;91mPlease enter a valid number.\033[0m")

    # Close the database connection
    conn.close()
