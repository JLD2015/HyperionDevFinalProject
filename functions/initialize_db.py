import sqlite3


def initialize_db():
    # This will create the database file if it doesn't exist
    conn = sqlite3.connect('econome.db')
    cursor = conn.cursor()

    # Create the Categories table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Categories (
            CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Type TEXT NOT NULL CHECK (Type IN ('Expense', 'Income'))  -- Ensures only 'Expense' or 'Income' can be stored
        )
    ''')

    # Create the Expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Expenses (
            ExpenseID INTEGER PRIMARY KEY AUTOINCREMENT,
            CategoryID INTEGER,
            Amount REAL NOT NULL,
            Date TEXT NOT NULL,
            Description TEXT,
            FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
        )
    ''')

    # Create the Income table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Income (
            IncomeID INTEGER PRIMARY KEY AUTOINCREMENT,
            CategoryID INTEGER,
            Amount REAL NOT NULL,
            Date TEXT NOT NULL,
            Description TEXT,
            FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
        )
    ''')

    # Create the Budgets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Budgets (
            BudgetID INTEGER PRIMARY KEY AUTOINCREMENT,
            CategoryID INTEGER,
            Amount REAL NOT NULL,
            Period TEXT NOT NULL,
            FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
        )
    ''')

    # Create the Financial Goals table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FinancialGoals (
            GoalID INTEGER PRIMARY KEY AUTOINCREMENT,
            Description TEXT NOT NULL,
            TargetAmount REAL NOT NULL,
            CurrentAmount REAL NOT NULL,
            Deadline TEXT NOT NULL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
