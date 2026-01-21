from email_checker import check_email
from phone_checker import check_phone

while True:
    print("\n--- Email & Phone Checker ---")
    print("1. Check Email")
    print("2. Check Phone Number")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        email = input("Enter email: ")
        if check_email(email):
            print("✅ Valid Email")
        else:
            print("❌ Invalid Email")

    elif choice == "2":
        phone = input("Enter phone number: ")
        if check_phone(phone):
            print("✅ Valid Phone Number")
        else:
            print("❌ Invalid Phone Number")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
