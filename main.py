from editing import editing_menu
from training import training_mode
from testing import testing_mode


def main():

    while True:
        print("1. Editing Mode")
        print("2. Training Mode")
        print("3. Testing Mode")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            editing_menu()
        elif choice == "2":
            training_mode()
        elif choice == "3":
            testing_mode()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
