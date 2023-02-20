import datetime


class Loan:

    def __init__(self, loan_id, customer_id: int, book_id: int,
                 loan_date: datetime.date, expect_return_date: datetime.date):
        self._loan_id = loan_id
        self._expect_return_date = expect_return_date
        self._loan_date = loan_date
        self._book_id = book_id
        self._customer_id = customer_id
        self._return_date = None

        # True = book is loan
        self._loan_status = True

    def get_customer_id(self):
        return self._customer_id

    def get_book_id(self):
        return self._book_id

    def get_loan_id(self):
        return self._loan_id

    def get_loan_date(self):
        return self._loan_date

    def get_loan_status(self):
        return self._loan_status

    def get_expect_return_date(self):
        return self._expect_return_date

    def set_expect_return_date(self, new_date):
        self._expect_return_date = new_date

    def get_return_date(self):
        return self._return_date

    def set_return_date(self, return_date):
        self._return_date = return_date

    def book_returned(self):
        self._loan_status = False
        self.set_return_date(datetime.date.today())

    @staticmethod
    def max_return_date(loan_date: datetime.date, max_days: int):
        return loan_date + datetime.timedelta(days=max_days)

    @staticmethod
    def create_loan_id(loan_dict):
        return len(loan_dict)

    def __str__(self):
        return f"\nCustomer: {self._customer_id}\nBook: {self._book_id}\nLoan Date: {self._loan_date}\n" \
               f" Expect return Date: {self._expect_return_date}\nStatus Loan: {self._loan_status}\n" \
               f"The date book was returned: {self._return_date}\n "

    def __repr__(self):
        return self.__str__()



