import datetime


class Book:

    def __init__(self, book_id: int, name: str, author: str, year_published: int, book_type: int):
        self._year_published = year_published
        self._author = author
        self._name = name
        self._book_id = book_id
        self._book_type = book_type

        # False = book is not loan
        self._book_loan_status = False

    def get_boo_id(self):
        return self._book_id

    def get_book_name(self):
        return self._name

    def get_author(self):
        return self._author

    def get_year_published(self):
        return self._year_published

    def get_book_type(self):
        return self._book_type

    def set_year_published(self, year):
        self._year_published = year

    @staticmethod
    def get_max_loan_time(book_type):
        if book_type == 1:
            return 10

        elif book_type == 2:
            return 5

        elif book_type == 3:
            return 2

    def get_book_status(self):
        return self._book_loan_status

    def book_is_loan(self):
        self._book_loan_status = True

    def book_is_return(self):
        self._book_loan_status = False

    @staticmethod
    def create_book_id(book_dict):
        return len(book_dict)

    @staticmethod
    def check_if_booktype_correct(book_type):
        return 1 <= book_type <= 3

    def __str__(self):
        return f"\n<ID: {self._book_id}\nName: {self._name}\nAuthor: {self._author}\n" \
               f"Year Publish: {self._year_published}>\nStatus Loan: {self._book_loan_status}\n"

    def __repr__(self):
        return self.__str__()


