import classes
import decorators



@decorators.input_error
def add_contact(name: str, phone: str):
    name_obj = classes.Name(name)
    if not phone:
        record = classes.Record(name_obj)
        classes.contact_book.add_record(record)
        result = f'Contact: {name} have been created!'
    elif name in classes.contact_book.data.keys():
        result = 'This contact exist in "Address book". Use change command!'
    else:
        phone_obj = classes.Phone(phone)
        record = classes.Record(name_obj, phone_obj)
        classes.contact_book.add_record(record)
        result = f'Contact: {name} have been created with phone: {phone}!'
    return result


@decorators.input_error
def change_contact(name: str, phone: str):
    if name not in classes.contact_book.data.keys():
        result = f'Contact {name} not found in Address book!'
        return result
    elif name in classes.contact_book.data and phone not in classes.contact_book.data[name].get_list_phones():
        phone_obj = classes.Phone(phone)
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
        result += f'Name: {key:<12}| Phone: {value.show_all_pnone()}\n' 
    return result
