from functions.functions_contact import *
from address_book.address_book import AddressBook
from functions.functions_birthday import *
from utils.utils import *
from contacts.contacts import *


def main():
    book=AddressBook()
    print("Welcome to the assistant bot!😎")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?😊")
            elif command == "add":
                print(add_contact(args,book))
            elif command == "change":
                print(change_contact(args,book))
            elif command == "phone":
                print(show_phone(args[0], book))
            elif command == "all":
              print(show_all(book))
            elif command == "add-birthday":                
                print(add_birthday(args,book))
            elif command == "show-birthday":
                print(show_birthday(args,book))
            elif command == "birthdays":
               print (birthdays(book))
            elif command == "delete":
                print(delete_contact(args, book)) 
            else:
                print("Invalid command.😴")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")




if __name__ == "__main__":
    main()