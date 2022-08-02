#Functions and Variables

from numpy import number


def books_and_copies(count_books, count_copies):
    print("There are %d books" % count_books)
    print("There are %d copies" % count_copies)
    print("These are enough for a month")
    print("Let's go")


#books_and_copies(12, 30)
# or
number_of_books = 11
number_of_copies = 10
books_and_copies(number_of_books, number_of_copies)
books_and_copies(number_of_books + 10, 10+2)
