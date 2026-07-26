import json
import os
import base64

FILE_NAME = "passwords.json"


def load_accounts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


accounts = load_accounts()


def encrypt(password):
    return base64.b64encode(password.encode()).decode()


def decrypt(password):
    return base64.b64decode(password.encode()).decode()


def add_account():

    print("\n=== Add Account ===")

    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    for account in accounts:
        if account["website"].lower() == website.lower():
            print("Account already exists.")
            return

    accounts.append({
        "website": website,
        "username": username,
        "password": encrypt(password)
    })

    save_accounts(accounts)

    print("Account saved successfully.")


def view_accounts():

    print("\n=== Saved Accounts ===")

    if not accounts:
        print("No accounts found.")
        return

    for account in accounts:

        print("-" * 35)
        print(f"Website : {account['website']}")
        print(f"Username: {account['username']}")
        print(f"Password: {decrypt(account['password'])}")

def search_account():

    print("\n=== Search Account ===")

    website = input("Enter Website: ").lower()

    for account in accounts:

        if account["website"].lower() == website:

            print("-" * 35)
            print(f"Website : {account['website']}")
            print(f"Username: {account['username']}")
            print(f"Password: {decrypt(account['password'])}")
            return

    print("Account not found.")


def delete_account():

    print("\n=== Delete Account ===")

    website = input("Enter Website: ").lower()

    for account in accounts:

        if account["website"].lower() == website:

            accounts.remove(account)

            save_accounts(accounts)

            print("Account deleted successfully.")
            return

    print("Account not found.")


while True:

    print("\n" + "=" * 40)
    print("       PASSWORD MANAGER")
    print("=" * 40)
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        delete_account()

    elif choice == "5":
        print("Thank you for using Password Manager.")
        break

    else:
        print("Invalid choice. Please try again.")
