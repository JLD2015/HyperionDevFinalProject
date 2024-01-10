import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_dashboard():
    conn = sqlite3.connect('econome.db')

    # Fetching data
    df_income = pd.read_sql_query("SELECT * FROM Income", conn)
    df_expenses = pd.read_sql_query("SELECT * FROM Expenses", conn)
    df_goals = pd.read_sql_query("SELECT * FROM FinancialGoals", conn)

    # Close the database connection
    conn.close()

    # Setting Seaborn style
    sns.set(style='whitegrid')

    # Creating subplots
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))

    # Income and Expenses Bar Chart
    df_summary = pd.DataFrame({'Total Income': df_income['Amount'].sum(),
                               'Total Expenses': df_expenses['Amount'].sum()}, index=[0])
    sns.barplot(data=df_summary, ax=axes[0], palette='pastel')
    axes[0].set_title('Income vs Expenses', fontsize=16, color='blue')
    axes[0].set_ylabel('Amount', fontsize=14)

    # Top Expense Categories
    top_expenses = df_expenses.groupby(
        'CategoryID')['Amount'].sum().nlargest(5)
    top_expenses.plot(kind='bar', ax=axes[1], color='skyblue')
    axes[1].set_title('Top Expense Categories', fontsize=16, color='green')
    axes[1].set_ylabel('Amount', fontsize=14)

    # Financial Goals Progress
    df_goals['Progress'] = (df_goals['CurrentAmount'] /
                            df_goals['TargetAmount']) * 100
    sns.barplot(x='Progress', y='Description',
                data=df_goals, ax=axes[2], palette='husl')
    axes[2].set_title('Financial Goals Progress', fontsize=16, color='purple')
    axes[2].set_xlabel('Progress %', fontsize=14)

    # Adjust layout
    plt.tight_layout()

    # Save the figure
    plt.savefig('financial_dashboard.png')
    print(
        "\n\033[1;92mDashboard generated and saved as 'financial_dashboard.png'.\033[0m\n")
