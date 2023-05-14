from collections import UserDict
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
        self.__value = new_value
 

class Record():
    def __init__(self, name: Name):
        self.name_obj = name
        self.phone_objs = []

        
 
    def add_phone(self, phone: Phone):
        self.phone_objs.append(phone)
    
    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday


    def change_phone(self, phone, new_phone):
        for object in self.phone_objs:
            if phone == object.value:
                object.value = new_phone

    def remove_phone(self, phone):
        for object in self.phone_objs:
            if phone == object.value:
                self.phone_objs.remove(object)

        
    def show_all_pnone(self):
        if not self.phone_objs:
                return ''
        for object in self.phone_objs:
            if object is self.phone_objs[0]:
                phone_list = ''
                phone_list += object.value
            else:
                phone_list += ', ' + object.value
        return phone_list
        
    def get_list_phones(self):
        phones_list = []
        for object in self.phone_objs:
            phones_list.append(object.value)
        return phones_list
    
    def get_name(self):
        return self.name_obj.value

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    def add_record(self, record: Record):
        self.data.update({record.get_name(): record})
        print(self.data)
        return self.data
    

contact_book = AddressBook()


if __name__ == '__main__':
    address_dict = AddressBook()

    user_1_name = Name('Sasha')
    user_2_name = Name('Jeck')

    user_date_1 = Record(user_1_name)
    user_date_2 = Record(user_2_name)

    address_dict.update({user_date_1.name_obj.contact_name: user_date_1})
    address_dict.update({user_date_2.name_obj.contact_name: user_date_2})

    print(address_dict)
    user_1_phone = '+380673528473'
    user_2_phone = '+380677284032'
    user_date_1.add_phone(user_1_phone)
    user_date_1.add_phone(user_2_phone)
   

