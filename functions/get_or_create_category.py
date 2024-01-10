import sqlite3

def get_or_create_category(category_type):
    conn = sqlite3.connect('econome.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT CategoryID, Name FROM Categories WHERE Type = ?", (category_type,))
    categories = cursor.fetchall()

    if categories:
        print("\033[1mAvailable Categories:\033[0m")
        for category in categories:
            print(f"{category[0]}: {category[1]}")
        print("\n")
    else:
        print(
            f"\nNo {category_type.lower()} categories available. Please add a category first.\n")

    while True:
        try:
            category_id = int(
                input(f"Enter the category ID (or 0 to add a new category): "))

            if category_id == 0:
                new_category_name = input(
                    f"\nEnter the name of the new {category_type.lower()} category: ").strip()
                cursor.execute(
                    "SELECT CategoryID FROM Categories WHERE Name = ? AND Type = ?", (new_category_name, category_type))
                existing_category = cursor.fetchone()

                if existing_category:
                    print(
                        f"Category '{new_category_name}' already exists with ID {existing_category[0]}")
                    conn.close()
                    return existing_category[0]
                else:
                    cursor.execute(
                        "INSERT INTO Categories (Name, Type) VALUES (?, ?)", (new_category_name, category_type))
                    conn.commit()
                    print(f"\nNew category '{new_category_name}' added.")
                    new_id = cursor.lastrowid
                    conn.close()
                    return new_id
            else:
                cursor.execute(
                    "SELECT Name FROM Categories WHERE CategoryID = ? AND Type = ?", (category_id, category_type))
                if cursor.fetchone():
                    conn.close()
                    return category_id
                else:
                    print(
                        "\033[1m\nInvalid CategoryID. Please enter a valid number or 0 to add a new category.\n\033[0m")
        except ValueError:
            print("\033[1m\nInvalid input. Please enter a valid number.\n\033[0m")
