import datetime

from my_library.address import Address
from my_library.book import Book
from my_library.customer import Customer
from my_library.library import Library
from my_library.loan import Loan


def library_test():
    library = Library("My Book", Address("Reshon-le-zion", "Anilewich", "3"))
    book = library.add_book("name", "author", year_published=2000, book_type=3)
    book2 = library.add_book("book name", "author", year_published=2000, book_type=3)
    customer = library.add_customer(123, "name", "last name", Address("city", "street", "3"),
                                    "name@gmail.com)", datetime.date(year=1996, month=8, day=21))

    assert len(library.get_all_books()) == 2

    library.loan_a_book(123, 100, datetime.date.today())

    assert library.get_book_by_id(100).get_book_name() == "name"

    assert library.get_book_by_id(100).get_book_status() is True

    assert library.get_loan_by_id(2000).get_expect_return_date() == datetime.date(year=2023, month=2, day=22)

    assert library.get_loan_by_id(2000).get_return_date() is None

    assert library.get_loan_by_id(2000).get_loan_status() is True

    assert library.get_book_by_id(101).get_book_status() is False

    library.return_a_book(2000, 100)

    assert library.get_book_by_id(100).get_book_status() is False

    assert library.get_loan_by_id(2000).get_return_date() == datetime.date(year=2023, month=2, day=20)

    assert library.get_loan_by_id(2000).get_loan_status() is False

def book_test():

    book = Book(123, "name", "author", year_published=2000, book_type=3)

    assert book.get_max_loan_time(3) == 2

    assert book.get_book_status() is False

    book.book_is_loan()

    assert book.get_book_status() is True

    book.book_is_return()

    assert book.get_book_status() is False


def customer_test():

    customer = Customer(123, "name", "last name", Address("city", "street", "3"),
                        "name@gmail.com)", datetime.date(year=1996, month=8, day=21))

    assert customer.get_whole_name() == "name last name"


def loan_test():

    assert Loan.max_return_date(datetime.date.today(), 5) == datetime.date(year=2023, month=2, day=25)


if __name__ == "__main__":
    library_test()
    book_test()
    customer_test()
    loan_test()







