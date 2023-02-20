import datetime

from my_library.address import Address


class Customer:

    def __init__(self, customer_id: int, name: str, last_name: str,
                 address: Address, email: str, birth_day: datetime.date):
        self._last_name = last_name
        self._birth_day = birth_day
        self._email = email
        self._address = address
        self._name = name
        self._customer_id = customer_id

    def get_id(self):
        return self._customer_id

    def get_whole_name(self):
        return f"{self._name} {self._last_name}"

    def set_whole_name(self, name, last_name):
        self._name = name
        self._last_name = last_name

    def get_email(self):
        return self._email

    def get_birth_date(self):
        return self._birth_day

    def get_address(self):
        return self._address

    def set_address(self, new_city, new_street, new_building_num):
        self._address = Address.change_address(new_city, new_street, new_building_num)

    def __str__(self):
        return f"\n<ID: {self._customer_id}\nWhole Name: {self._name} {self._last_name}\n" \
               f"Address: {self._address}\nEmail: {self._email}\nBirth Date: {self._birth_day}>\n"

    def __repr__(self):
        return self.__str__()


