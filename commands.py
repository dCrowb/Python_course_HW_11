import classes
import decorators



@decorators.input_error
def add_contact(name: str, phone, birthday):
    name_obj = classes.Name(name)
    record = classes.Record(name_obj)
    result = f'Contact: {name} have been created'
    if phone:
        phone_obj = classes.Phone()
        phone_obj.value = phone
        if phone_obj.value == 'Incorrect phone number':
            return 'Incorrect phone number'
        record.add_phone(phone_obj)
        result +=  f'with phone: {phone}'
    if birthday:
        birthday_obj = classes.Birthday()
        birthday_obj.value = birthday
        if not birthday_obj.value:
            return 'Incorrect birthday!'
        record.add_birthday(birthday_obj)
        result += f' and birthday: {birthday}!'
    classes.contact_book.add_record(record)
    return result


@decorators.input_error
def change_contact(name: str, phone: str):
    if name not in classes.contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in classes.contact_book.data and phone not in classes.contact_book.data[name].get_list_phones():
        phone_obj = classes.Phone()
        phone_obj.value = phone
        if phone_obj.value == 'Incorrect phone number':
            return 'Incorrect phone number'
        classes.contact_book.data[name].add_phone(phone_obj)
        result = f'Contact {name} has been added phone: {phone}!'
    elif name in classes.contact_book.data and phone in classes.contact_book.data[name].get_list_phones():
        result = f'Contact: {name} with phone: {phone} already in Address book!'
    return result



@decorators.input_error
def remove_phone(name: str, phone: str):
    if name not in classes.contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in classes.contact_book.data and phone in classes.contact_book.data[name].get_list_phones():
        classes.contact_book.data[name].remove_phone(phone)
        result = f'Contact {name} has been removed phone: {phone}!'
    return result


@decorators.input_error
def replace_phone(name: str, phone: str, new_phone: str):
    if name not in classes.contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in classes.contact_book.data and phone in classes.contact_book.data[name].get_list_phones():
        new_phone_obj = classes.Phone()
        new_phone_obj.value = new_phone
        if new_phone_obj.value == 'Incorrect phone number':
            return 'Incorrect phone number'
        classes.contact_book.data[name].change_phone(phone, new_phone)
        result = f'Contact {name} has been changed phone: {phone} on phone: {new_phone}!'
    return result

    

@decorators.input_error   
def show_contact(value: str, flag: str):
    if flag == 'name' and value in classes.contact_book.data.keys():
        result =  f'Phones{classes.contact_book.data[value].get_list_phones()}'
    else:
        for key, contacts in classes.contact_book.data.items():
            if value in contacts.get_list_phones():
                name = key
                result = f'Contact name: {name}!'
            else:
                result = f"Contact with this name or phone doesn't exist in Address book"
    return result


def end_process():
    mesage = f'Good bye!'
    return mesage


def greeting_user():
    mesage = f'How can I help you?'
    return mesage


@decorators.input_error
def show_all_contacts():
    result = ''
    for key, value in classes.contact_book.data.items():
        result += f'Name: {key:<5} | {value.show_all_data()}' 
    return result


def change_birthday(name: str, birthday: str):
    if name not in classes.contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in classes.contact_book.data:
        birthday_obj = classes.Birthday()
        birthday_obj.value = birthday
        if not birthday_obj.value:
            return 'Incorrect birthday!'
        classes.contact_book.data[name].add_birthday(birthday_obj)
        result = f'Contact {name} has been added phone: {birthday}!'
    return result


def days_to_birthday(name: str):
    result = classes.contact_book.data[name].days_to_birthday()
    return result


@decorators.input_error
def show_contacts_page():
    if len(classes.contact_book.data) < 1:
        return 'Address book is empty'
    else:
        page_size = 5
        start_point = 0
        for page in classes.contact_book.iterator(page_size):
            for item in page:
                result = f'Name: {item.get_name():>5} | {item.show_all_data()}'
                print(result)
            while True:
                key = input('Next page - n. Quit - q:')
                if key == 'q':
                    return 'User stopped process'
                elif key == 'n':
                    break


        
  




# def show_all_phones_handler(user_data: tuple, address_book: Address_Book):
#     if address_book.recordsCount > 0:
#         responseMessage = "Current address book contains:\n"
#         page_size = 2
#         start_position = 1
#         for book in address_book.iterator(page_size):
#             for item in enumerate(book, start_position):
#                 position = item[0]
#                 user_name = item[1].user_name.value
#                 phones = ", ".join(
#                     [field.value for field in item[1].fields if isinstance(field, Phone)])
#                 responseMessage += f"{position}. {user_name}: {phones}\n"
#             start_position += page_size
#     else:
#         responseMessage = "Current address book is empty.\n"
#     return responseMessage