import sqlite3
import pandas as pd


def export_data():
    conn = sqlite3.connect('econome.db')

    # Define the tables you want to export
    tables = ['Income', 'Expenses', 'FinancialGoals',
              'Categories', 'Budgets']  # Add other tables if needed

    # Open a file to write all data
    with open('all_data_export.csv', 'w') as file:
        for table in tables:
            # Write the table name as a header
            file.write(f"\n{table}\n")

            # Read the table into a DataFrame
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)

            # Write the DataFrame to CSV format and into the file
            df.to_csv(file, index=False)

            # Add a separator after each table for clarity
            file.write("\n" + "-" * 50 + "\n")

    # Close the database connection
    conn.close()

    print(
        "\n\033[1;92mAll data exported successfully to 'all_data_export.csv'.\033[0m\n")
