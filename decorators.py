import classes

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except SystemExit:
            print('Incorect command')
        except classes.PhoneError:
            print('Incorrect phone number')
            return None
        # except AttributeError:
        #     print('Incorect argument!')
        except ValueError:
            print('Give me name and phone please')
        except KeyError:
            print('User doesn`t exist')
        except IndexError:
            print('Enter user name')
        except UnboundLocalError:
            print('Try again')
    return inner