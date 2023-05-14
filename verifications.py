import re
import decorators


@decorators.input_error
def check_phone_number(phone: str):
    phone = phone.replace(' ', '').replace('-', '')
    check_phone = re.search(r'[+][0-9]{12}|[0-9]{10}', phone)
    if check_phone and len(phone) == 13:
        return phone
    elif check_phone and len(phone) == 10:
        phone = '+38' + phone
        return phone
    else:
        raise decorators.PhoneError