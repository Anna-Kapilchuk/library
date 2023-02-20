
class Address:

    def __init__(self, city: str, street: str, building_num: str):
        self._building_num = building_num
        self._street = street
        self._city = city

    def __str__(self):
        return f"{self._city}, {self._street} {self._building_num}"

    def change_address(self, city: str, street: str, building_num: str):
        self._city = city
        self._street = street
        self._building_num = building_num


