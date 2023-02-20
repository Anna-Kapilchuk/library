import datetime
import os.path
import pickle

from my_library.address import Address
from my_library.book import Book
from my_library.library import Library
from my_library.library_exception import *

if __name__ == "__main__":

    library = None

    try:
        if not os.path.exists("library_data.pickle"):
            library = Library("My Book", Address("Reshon-le-zion", "Anilewich", "3"))

        else:
            with open("library_data.pickle", "rb") as f:
                library = pickle.load(f)
    except Exception:
        print("cannot create or load library_data.pickle file")

    print("Hello, Welcome to My Book library")

    while True:

        try:
            print("\nMain Menu:\n1: books\n2: customers\n3: loan\n4: Exit")
            # print("\nMain Manu:\n1: Add a book\n2: find a book\n3: remove a book\n4: add customer\n"
            #       "5: find customer\n6: remove customer\n7: update customer\n8: loan a book\n""9: return a book\n"
            #       "10: get loans\n11: Exit")

            choice = int(input("What do you want to do?\n-- "))

            # books
            if choice == 1:

                print("\n1: Add a book\n2: find a book\n3: remove a book\n4: back to main menu\n")
                choice2 = int(input("what do you want to do?\n--"))

                # add book
                if choice2 == 1:
                    name = input("Add the name of the book: ").capitalize()
                    author = input("Add the author of the book: ").capitalize()
                    year_published = int(input("Insert year_published: "))
                    book_type = int(input("Insert max time that book can be loan\n1: 10 days\n"
                                          "2: 5 days\n3: 2 days\n"))
                    library.add_book(name, author, year_published, book_type)
                    print("New book was added\n\n")
                    continue

                # find a book
                elif choice2 == 2:
                    second_choice = int(input("\nHow do you like to find the book:\n1: show all books\n"
                                              "2: find book by name\n3: find books by author\n"
                                              "4: find books by year\n--"))

                    # show all the books
                    if second_choice == 1:
                        print(library.get_all_books())

                    # find book by name
                    elif second_choice == 2:
                        book_name = input("Insert the book name: ").capitalize()
                        print(library.get_book_by_name(book_name))

                    # find books by author
                    elif second_choice == 3:
                        author = input("Insert author name: ")
                        print(library.get_books_by_author(author))

                    # find book by year
                    elif second_choice == 4:
                        book_year = int(input("Insert publish year: "))
                        print(library.get_book_by_year(book_year))

                    # wrong value
                    else:
                        raise ValueError

                # remove book
                elif choice2 == 3:
                    book_id = int(input("insert book id that you want to remove: "))
                    library.remove_book(book_id)
                    print(f"book {library.get_book_by_id(book_id).get_book_name()} was removed")

                # back to main menu
                elif choice2 == 4:
                    continue

                # wrong value
                else:
                    raise ValueError()

            # customer
            elif choice == 2:

                print("\n1: add customer\n2: find customer\n3: remove customer\n"
                      "4: update customer\n5: back to main menu")

                choice3 = int(input("what do you want to do?\n--"))

                # add customer
                if choice3 == 1:
                    customer_id = int(input("Insert customer id: "))
                    name = input("first name: ").capitalize()
                    last_name = input("last name: ").capitalize()
                    city = input("city: ")
                    street = input("street: ")
                    building_num = input("building number: ")
                    email = input("E-mail: ")
                    birth_year = int(input("birth year: "))
                    birth_month = int(input("birth month: "))
                    birth_day = int(input("birth day: "))

                    library.add_customer(customer_id, name, last_name, Address(city, street, building_num),
                                         email, datetime.date(year=birth_year, month=birth_month, day=birth_day))

                # find customer
                elif choice3 == 2:
                    second_choice = int(input("\nHow do you like to find the customer:\n1: show all customers\n"
                                              "2: find customer by ID\n3: find customer by name\n--"))

                    # show all customers
                    if second_choice == 1:
                        print(library.get_all_customers())

                    # find customer by ID
                    elif second_choice == 2:
                        customer_id = int(input("Insert customer id: "))
                        print(library.get_customer_by_id(customer_id))

                    # find customer by name
                    elif second_choice == 3:
                        customer_name = input("Insert customer name: ")
                        print(library.get_customer_by_name(customer_name))

                    # wrong value
                    else:
                        raise ValueError()

                # remove customer
                elif choice3 == 3:
                    customer_id = int(input("Insert customer id: "))
                    library.remove_customer(customer_id)
                    print(f"customer {library.get_customer_by_id(customer_id).get_whole_name()} was removed")

                # update customer
                elif choice3 == 4:
                    second_choice = int(input("\n1: update customer whole name\n2: update customer address\n--"))
                    customer_id = int(input("Insert customer ID: "))

                    # update customer whole name
                    if second_choice == 1:
                        new_name = input("Insert new name: ").capitalize()
                        new_last_name = input("Insert new last name: ").capitalize()
                        library.update_customer_whole_name(customer_id, new_name, new_last_name)

                    # update customer address
                    elif second_choice == 2:
                        new_city = input("Insert customer new city: ")
                        new_street = input("Insert customer new street: ")
                        new_building_num = int(input("insert customer new building number: "))
                        library.update_customer_address(customer_id, new_city, new_street, new_building_num)

                    # wrong value
                    else:
                        raise ValueError()

                # back to main menu
                elif choice3 == 5:
                    continue

                # wrong value
                else:
                    raise ValueError()

            # loan
            elif choice == 3:

                print("\n1: loan a book\n2: return a book\n3: get loans\n4: back to main menu\n")
                choice4 = int(input("what do you want to do?\n--"))

                # loan a book
                if choice4 == 1:
                    customer_id = int(input("Insert customer id: "))
                    book_id = int(input("Insert book id: "))
                    loan_id = library.loan_a_book(customer_id, book_id, datetime.date.today())

                    print(f"customer {library.get_customer_by_id(customer_id).get_whole_name()}"
                          f" loaned book {library.get_book_by_id(book_id).get_book_name()}, ID of loan is {loan_id}"
                          f" the book must be returned in"
                          f" {Book.get_max_loan_time(library.get_book_by_id(book_id).get_book_type())} days")

                # return a book
                elif choice4 == 2:
                    loan_id = int(input("Insert the loan ID: "))
                    book_id = int(input("Insert the book ID: "))
                    library.return_a_book(loan_id, book_id)
                    print(f"book {library.get_book_by_id(book_id).get_book_name()} was returned")

                # get loans
                elif choice4 == 3:
                    second_choice = int(input("\n1: Show all loans\n2: find loan by ID\n"
                                              "3: find loan by customer ID\n4: get late loan\n--"))

                    # show all loans
                    if second_choice == 1:
                        print(library.get_all_loan())

                    # find loan by ID
                    elif second_choice == 2:
                        loan_id = int(input("Insert loan ID: "))
                        print(library.get_loan_by_id(loan_id))

                    # find loan by customer
                    elif second_choice == 3:
                        customer_id = int(input("Insert customer ID: "))
                        print(library.get_loan_by_customer(customer_id))

                    # get late loan
                    elif second_choice == 4:
                        print(library.get_late_loans())

                # back to main menu
                elif choice4 == 4:
                    continue

                # wrong value
                else:
                    raise ValueError()

            # Exit
            elif choice == 4:
                print("thank you for using our library system")
                break

        except BookCannotBeLoan:
            print("You cannot loan this book, this book already loaned")

        except CustomerNotFound:
            print("customer not found, back to main menu")

        except BookIdError:
            print("book ID not found, back to main menu")

        except CustomerAlreadyExists:
            print("The customer exists in the system")

        except BookNotLoaned:
            print("you cannot return book that did not loan")

        except IncorrectYear:
            print("you add incorrect year")

        except ValueError:
            print("you insert wrong value, back to main menu")

        except Exception:
            print("Unknown error, back to main menu")

        finally:
            with open("library_data.pickle", "wb") as f:
                pickle.dump(library, f)
