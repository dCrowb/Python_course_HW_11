from collections import UserDict
import datetime
import verifications


class Field():
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return self.value
    



class Name(Field):
    def __init__(self, value):
        super().__init__(value)



class Phone(Field):
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        new_value = verifications.check_phone_number(new_value)
        if not new_value:
            return
        else:
            self.__value = new_value


class Birthday(Field):
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        new_value = verifications.check_birthday(new_value)
        if not new_value:
            return
        else:
            self.__value = new_value
 

class Record():
    def __init__(self, name: Name):
        self.name_obj = name
        self.phone_objs = []

        
 
    def add_phone(self, phone: Phone):
        self.phone_objs.append(phone)
    
    def add_birthday(self, birthday: Birthday):
        self.birthday_obj = birthday


    def change_phone(self, phone, new_phone):
        for object in self.phone_objs:
            if phone == object.value:
                object.value = new_phone

    def remove_phone(self, phone):
        for object in self.phone_objs:
            if phone == object.value:
                self.phone_objs.remove(object)

        
    def show_all_data(self):
        if not self.phone_objs:
                return f'Birthday: {self.get_birthday():<12}| Phone: empty\n'
        for object in self.phone_objs:
            if object is self.phone_objs[0]:
                phone_list = ''
                phone_list += object.value
            else:
                phone_list += ', ' + object.value
        result = f'Birthday: {self.get_birthday():<12}| Phone: {phone_list}\n'
        return result
        
    def get_list_phones(self):
        phones_list = []
        for object in self.phone_objs:
            phones_list.append(object.value)
        return phones_list
    
    def get_name(self):
        return self.name_obj.value
    

    def get_birthday(self):
        if hasattr(self, 'birthday_obj'):
            return self.birthday_obj.value.strftime('%d.%m.%Y')
        else:
            return 'unknown'
    
    def days_to_birthday(self):
        if hasattr(self, 'birthday_obj'):
            birthday = self.get_birthday()
            current_date = datetime.datetime.now().date()
            current_year = current_date.strftime('%Y')
            birthdate = f'{birthday[0:6]}{current_year}'
            birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y').date()
            if current_date == birthdate:
                return f'Birthday is today'
            elif current_date > birthdate:
                birthdate = birthdate.replace(year=birthdate.year + 1)
            result = birthdate - current_date
            return f'Birthday in {result.days} days'
        else:
            return 'Birthday: unknown'



class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    def add_record(self, record: Record):
        self.data.update({record.get_name(): record})
        print(self.data)
        return self.data
    
    def iterator(self, page_size=5):
        values = list(self.data.values())
        for i in range(0, len(values), page_size):
            start_point = i
            end_point = i + page_size
            i += page_size
            yield values[start_point:end_point]

    

contact_book = AddressBook()


if __name__ == '__main__':
    address_dict = AddressBook()
    user_1 = Record(Name('aaa'))
    user_1_phone = Phone()
    user_1_phone.value = '+380974653421'
    user_2 = Record(Name('bbb'))
    user_2_phone = Phone()
    user_2_phone.value = '+380974353421'
    user_1.add_phone(user_1_phone)
    user_2.add_phone(user_2_phone)
    address_dict.add_record(user_1)
    address_dict.add_record(user_2)


