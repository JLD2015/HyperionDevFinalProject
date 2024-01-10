from datetime import datetime


def validate_date(date_text, allow_future=False):
    try:
        input_date = datetime.strptime(date_text, '%Y-%m-%d')
        current_date = datetime.now()
        if not allow_future and input_date > current_date:
            print("\033[1m\nDate cannot be in the future.\n\033[0m")
            return False
        return True
    except ValueError:
        print(
            "\033[1m\nInvalid date format. Please enter the date in YYYY-MM-DD format.\n\033[0m")
        return False
