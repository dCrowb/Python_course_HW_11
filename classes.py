from collections import UserDict


class Field():
    pass


class Name(Field):
    def __init__(self, name):
        self.contact_name = name

    def __repr__(self) -> str:
        return self.contact_name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def __repr__(self) -> str:
        return self.phone
        

class Record():
    def __init__(self, name: Name, phone=None):
        self.name_obj = name
        self.phone_objs = []
        if phone:
            self.add_phone(phone)
 
    def add_phone(self,phone: Phone):
        self.phone_objs.append(phone)

    def change_phone(self, phone, new_phone):
        for object in self.phone_objs:
            if phone == object.phone:
                object.phone = new_phone

    def remove_phone(self, phone):
        for object in self.phone_objs:
            if phone == object.phone:
                self.phone_objs.remove(object)

        
    def show_all_pnone(self):
        for object in self.phone_objs:
            if not object:
                return ''
            if object is self.phone_objs[0]:
                phone_list = ''
                phone_list += object.phone
            else:
                phone_list += ', ' + object.phone
        return phone_list
        
    def get_list_phones(self):
        phones_list = []
        for object in self.phone_objs:
            phones_list.append(object.phone)
        return phones_list
    
    def get_name(self):
        return self.name_obj.contact_name

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    def add_record(self, record: Record):
        self.data.update({record.get_name(): record})
        return self.data
    

class PhoneError(Exception):
    pass


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
   

