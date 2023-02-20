class LibraryException(Exception):
    pass


class BookCannotBeLoan(LibraryException):
    pass


class CustomerNotFound(LibraryException):
    pass


class BookIdError(LibraryException):
    pass


class CustomerAlreadyExists(LibraryException):
    pass


class BookNotLoaned(LibraryException):
    pass


class IncorrectYear(LibraryException):
    pass
