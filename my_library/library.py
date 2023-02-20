import datetime

from my_library.address import Address
from my_library.book import Book
from my_library.customer import Customer
from my_library.library_exception import *
from my_library.loan import Loan


class Library:

    def __init__(self, name: str, address: Address):
        self._address = address
        self._name = name
        self._books: dict[int, Book] = {}
        self._customers: dict[int, Customer] = {}
        self._loans: dict[int, Loan] = {}

    def get_library_name(self):
        return self._name

    def add_book(self, name: str, author: str, year_published: int,
                 book_type: int):

        # book ID starts at 100
        book_id: int = 100 + Book.create_book_id(self._books)

        # check if book ID in system
        if book_id in self._books:
            raise BookIdError()

        if not 1800 <= year_published <= 2023:
            raise IncorrectYear()

        # book type must be 1, 2 or 3
        if not Book.check_if_booktype_correct(book_type):
            raise ValueError()

        book: Book = Book(book_id, name, author, year_published, book_type)
        self._books[book_id] = book

    def get_book_by_id(self, book_id):
        return self._books.get(book_id)

    def get_book_by_name(self, book_name: str) -> list[Book]:

        ret_val: list = []

        for book_id, book in self._books.items():
            if book_name == book.get_book_name():
                ret_val.append(book)

        return ret_val

    def get_books_by_author(self, author: str) -> list[Book]:

        ret_val: list = []

        # going through a dict of books
        for bo_id, book in self._books.items():
            if book.get_author() == author:
                ret_val.append(book)

        return ret_val

    def get_book_by_year(self, year_publish: int) -> list[Book]:
        ret_val: list = []

        # going through a dict of books
        for bo_id, book in self._books.items():
            if book.get_year_published() == year_publish:
                ret_val.append(book)

        return ret_val

    def get_all_books(self) -> dict[int, Book]:
        return self._books

    def remove_book(self, book_id: int):

        # check if book ID not in books dict
        if book_id not in self._books:
            raise BookIdError()

        del self._books[book_id]

    def add_customer(self, customer_id: int, name: str, last_name: str, address: Address,
                     email: str, birth_day: datetime.date):

        if customer_id in self._customers:
            raise CustomerAlreadyExists()

        customer: Customer = Customer(customer_id, name, last_name, address, email, birth_day)
        self._customers[customer_id] = customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        return self._customers.get(customer_id)

    def get_customer_by_name(self, customer_name: str) -> list[Customer]:

        ret_val: list = []

        # going through a dict of customers
        for cus_id, customer in self._customers.items():
            if customer.get_whole_name() == customer_name:
                ret_val.append(customer)

        return ret_val

    def update_customer_whole_name(self, customer_id: int, new_name: str, new_last_name: str):

        customer: Customer = self._customers.get(customer_id)

        if not customer:
            raise CustomerNotFound()

        customer.set_whole_name(new_name, new_last_name)

    def update_customer_address(self, customer_id: int, new_city: str, new_street: str, new_building_num: int):
        customer: Customer = self._customers.get(customer_id)

        if not customer:
            raise CustomerNotFound()

        customer.set_address(new_city, new_street, new_building_num)

    def get_all_customers(self) -> dict[int, Customer]:
        return self._customers

    def remove_customer(self, customer_id: int):
        if customer_id not in self._customers:
            raise CustomerNotFound()

        del self._customers[customer_id]

    def get_all_loan(self) -> dict[int, Loan]:
        return self._loans

    def get_loan_by_id(self, loan_id: int) -> Loan:
        return self._loans.get(loan_id)

    def get_loan_by_customer(self, customer_id: int) -> list[Loan]:

        ret_val: list = []

        # going through a dict of loans
        for loan_id, loan in self._loans.items():
            if customer_id == loan.get_customer_id():
                ret_val.append(loan)

        return ret_val

    def get_late_loans(self):
        ret_val: list = []

        # going through a dict of loans
        for loan_id, loan in self._loans.items():
            if datetime.date.today() > loan.get_expect_return_date():
                ret_val.append(loan)

        return ret_val

    def loan_a_book(self, customer_id: int, book_id: int,
                    loan_date: datetime.date):

        if book_id not in self._books:
            raise BookIdError()

        book: Book = self._books.get(book_id)

        if book.get_book_status():
            raise BookCannotBeLoan()

        if customer_id not in self._customers:
            raise CustomerNotFound()

        # loan ID starts at 2000
        loan_id: int = 2000 + Loan.create_loan_id(self._loans)

        loan: Loan = Loan(loan_id, customer_id, book_id, loan_date,
                          Loan.max_return_date(loan_date,
                                               Book.get_max_loan_time(self._books.get(book_id).get_book_type())))

        self._loans[loan_id] = loan

        # status book: True
        book.book_is_loan()

        return loan_id

    def return_a_book(self, loan_id: int, book_id: int):

        book: Book = self._books.get(book_id)
        loan: Loan = self._loans.get(loan_id)

        if not book.get_book_status():
            raise BookNotLoaned()

        # status book: False
        book.book_is_return()

        # status loan : False
        loan.book_returned()

