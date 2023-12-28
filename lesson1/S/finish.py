class PersonInfo:
    def value(self):
        raise NotImplementedError


class PersonPhoneNumber(PersonInfo):
    def __init__(self, phone: str, operator_code: str):
        if operator_code == '067':
            raise ValueError("Invalid operator code")
        self.phone = phone
        self.operator_code = operator_code

    def value(self):
        return f"+38({self.operator_code}){self.phone}"


class PersonAddress(PersonInfo):
    def __init__(self, city: str, street: str):
        self.city = city
        self.street = street

    def value(self):
        return f"{self.city}, {self.street}"


class Person:
    def __init__(self, name: str, phone: PersonPhoneNumber, address: PersonAddress):
        self.name = name
        self.phone = phone
        self.address = address

    def get_phone_number(self):
        return f"{self.name}: {self.phone.value()}"

    def get_address(self):
        return f"{self.name}: {self.address.value()}"


if __name__ == '__main__':
    phone = PersonPhoneNumber('022811244', '050')
    address = PersonAddress('Sofia', 'Bulgaria')
    person = Person("Alexander", phone, address)
    print(person.get_phone_number())
    print(person.get_address())
