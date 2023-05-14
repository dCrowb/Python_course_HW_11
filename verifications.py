import re
import decorators, classes

@decorators.input_error
def check_phone_number(phone: str):
    phone = phone.replace(' ', '').replace('-', '')
    check_phone = re.search(r'[+][0-9]{12}|[0-9]{10}', phone)
    if check_phone and (len(phone) == 13 or len(phone) == 10):
        return phone
    else:
        raise classes.PhoneError