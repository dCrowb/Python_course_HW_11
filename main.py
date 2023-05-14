import argparse
import decorators, verifications
from constants import (
    COMANDS_WITHOUT_ARGUMENTS,
    COMANDS_WITH_ARGUMENTS
)
from commands import (
    add_contact,
    remove_phone,
    replace_phone,
    change_contact,
    show_contact
)


def command_call(command: str, arguments: argparse):
    print(command)
    if command == 'add':
        result = add_contact(arguments.name, arguments.phone)
    elif command == 'change':
        if arguments.delete_phone:
            result = remove_phone(arguments.name, arguments.delete_phone)
        elif arguments.replace_phone:
            result = replace_phone(arguments.name, arguments.phone, arguments.replace_phone)
        elif arguments.phone and not arguments.replace_phone:
            result = change_contact(arguments.name, arguments.phone)
    elif command == 'show':
        if arguments.name:
            result = show_contact(arguments.name, 'name')
        elif arguments.phone:
            result = show_contact(arguments.phone, 'phone')
            
    return result

    

@decorators.input_error
def build_parser(arguments: str):
    parser = argparse.ArgumentParser(description="Contact book")
    parser.add_argument("-n", dest="name")
    parser.add_argument("-p", dest="phone")
    parser.add_argument("-r", dest="replace_phone")
    parser.add_argument("-d", dest="delete_phone")
    args = parser.parse_args(arguments.split())
    return args


def command_parser(user_input: str):
    command_elements = user_input.split(' ')
    if len(command_elements) < 2:
        arguments = None
        return command_elements[0], arguments
    else:
        arguments = user_input.split(' ', 1)[1]
        parsed_args = build_parser(arguments)
        return command_elements[0], parsed_args


def main():
    '''---------------------------
        add -n [name] -p [phone] - add new contact.
        change -n [name] -p [phone]- change existing contact.
        change -n [name] -d [phone]- remove existing phone.
        show -n [name] - show number or -p [phone] - show name.
        show_all - show all stored contacts and their numbers.
        To terminate the program, enter one of the following commands:
        good_bye
        close
        exit
        \n---------------------------'''

    while True:
        user_input = input('\nWait command #:').lower()
        command, arguments = command_parser(user_input)

        if command in COMANDS_WITHOUT_ARGUMENTS:
            result = COMANDS_WITHOUT_ARGUMENTS[command]()
            print(result)
            if result == 'Good bye!':
                break
        elif not arguments:
            print('Wrong command! Try again with arguments!')
        elif command in COMANDS_WITH_ARGUMENTS:
            if arguments.phone and not verifications.check_phone_number(arguments.phone):
                continue
            if arguments.replace_phone and not verifications.check_phone_number(arguments.replace_phone):
                continue
            if arguments.delete_phone and not verifications.check_phone_number(arguments.delete_phone):
                continue
            print(command_call(command, arguments))

        else:
            print('Wrong command! Try again!')



if __name__ == '__main__':
    main()