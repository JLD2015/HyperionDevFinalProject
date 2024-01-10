from datetime import datetime, timedelta


def calculate_available_budget(conn, period_days):
    cursor = conn.cursor()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=period_days)

    # Calculate total income for the period
    cursor.execute("SELECT SUM(Amount) FROM Income WHERE Date BETWEEN ? AND ?",
                   (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
    total_income = cursor.fetchone()[0] or 0

    # Calculate total expenses for the period
    cursor.execute("SELECT SUM(Amount) FROM Expenses WHERE Date BETWEEN ? AND ?",
                   (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
    total_expenses = cursor.fetchone()[0] or 0

    return total_income - total_expenses
