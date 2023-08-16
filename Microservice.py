#Microservice for partners book tracker

import os
import threading
import time

def findBook():
    check_search = open('findBook.txt', 'r')
    with check_search:
        check = check_search.read().lower()
        check_search.close()
        if check == 'searching':
            file = open('findBook.txt', 'w')
            file.close()
            book = open('books.txt', 'r')
            with book:
                book_info = book.read().lower()
                returnBook = book_info
                with open('foundBook.txt', 'w') as file:
                    file.write(returnBook)


def interval_function():
    while True:
        findBook()
        time.sleep(3)
interval_thread = threading.Thread(target=interval_function)
interval_thread.start()