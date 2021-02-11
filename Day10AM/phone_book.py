"""
File: phone_book.py
-----------------
This program allows the user to store and lookup phone numbers
in a phone book.  They can "add", "lookup" or "quit".
"""


def main():
    print("Welcome to Phone Book!  This program stores phone numbers of contacts.  You can add a new number, "
          "get a number,or quit ('add', 'lookup', 'quit').")
    print('Enter your command at the prompt.')

    phone_book = dict()

    while True:
        choice = input("(add', 'lookup', 'quit') > ").lower()

        if choice == 'add':
            name = input('name? ').lower()
            number = input('number? ')

            phone_book[name] = number

        elif choice == 'lookup':
            name = input('name? ').lower()

            if name in phone_book.keys():
                print(phone_book[name])

            else:
                print(name + ' not found.')

        elif choice == 'quit':
            quit()



if __name__ == '__main__':
    main()
