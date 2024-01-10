"""
The EconoMe app allows users to track their incomes and expanses.
They are able to make better informed financial decisions by effectively managing their finances.
"""

# <========== Imports ==========>
from functions.add_expense import add_expense
from functions.initialize_db import initialize_db
from functions.display_menu import display_menu
from functions.view_all_expenses import view_all_expenses
from functions.view_expenses_by_category import view_expenses_by_category
from functions.add_income import add_income
from functions.view_all_incomes import view_all_incomes
from functions.view_incomes_by_category import view_incomes_by_category
from functions.set_budget_for_category import set_budget_for_category
from functions.view_budget_for_category import view_budget_for_category
from functions.set_financial_goals import set_financial_goals
from functions.view_financial_goals_progress import view_financial_goals_progress
from functions.generate_dashboard import generate_dashboard
from functions.export_data import export_data

# Welcome the user to the program
print("\n\033[1m<========== Welcome to EconoMe ==========>\033[0m\n")

# Initialise the database
initialize_db()

# Program runs in a loop until the user exist the program
while True:

    # Display menu options to the user
    display_menu()

    # Convert the user's selction into an integer
    try:
        user_selection = int(input("Input : "))

        # Make sure the integer is in the valid range
        if 1 <= user_selection <= 13:

            if user_selection == 1:
                # Add expense
                add_expense()
                pass
            elif user_selection == 2:
                # View user expenses
                view_all_expenses()
                pass
            elif user_selection == 3:
                # View user expenses by category
                view_expenses_by_category()
                pass
            elif user_selection == 4:
                # Add income
                add_income()
                pass
            elif user_selection == 5:
                # View income
                view_all_incomes()
                pass
            elif user_selection == 6:
                # View income by category
                view_incomes_by_category()
                pass
            elif user_selection == 7:
                # Set a budget for a category
                set_budget_for_category()
                pass
            elif user_selection == 8:
                # View the budget for a specific category
                view_budget_for_category()
                pass
            elif user_selection == 9:
                # Set financial goals
                set_financial_goals()
                pass
            elif user_selection == 10:
                # View progress towards financial goals
                view_financial_goals_progress()
                pass
            elif user_selection == 11:
                # Generate a dashboard to give the user an overview of all of their financial information
                generate_dashboard()
                pass
            elif user_selection == 12:
                # Export all of the user's data
                export_data()
                pass
            elif user_selection == 13:
                # Exit the program
                print(
                    "\n\033[1m<========== Thank you for using EconoMe ==========>\033[0m\n")
                exit()

        else:
            print("\033[1m\nPlease select a number from 1 to 13\n\033[0m")

    except ValueError:
        print("\033[1m\nPlease enter a valid number.\n\033[0m")
