#Implementation of Microservice for Partner Project

import PySimpleGUI as sg
import webbrowser
import os.path


def find_book():
    
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text="Hello! I can help you find a book!", font='Arial, 12'), sg.Push()],
        [sg.Push(), sg.Text(text='Please click the button below to understand how this program works!', font='Arial, 12'), sg.Push()],
        [sg.Push(), sg.Button('Understanding the Program!'), sg.Push()],
        [sg.Push(), sg.Button('Take me to the Book Finder!'), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window('Book Finder', layout, size=(500, 300))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close Window':
            break
        print(values)

        if event == 'Understanding the Program!':
            book_finder_help()

        if event == 'Take me to the Book Finder!':
            book_finder()



def book_finder_help():

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text('I am here to help you navigate this program!', font='Arial, 12'), sg.Push()],
        [sg.Push(), sg.Text('If you have recorded a book, I will be able to display that book for you.', font='Arial, 12'), sg.Push()],
        [sg.Push(), sg.Text('If you have not logged a book you are searching for, I will notify you that there is not a book in the tracker!', font=('Arial, 12')), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text('You will have the option to search by Title, Author, or genre and results will be displayed based on those items!', font='Arial, 12')],
        [sg.Push(), sg.Button('Let\'s Find a Book!'), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window('Book Help!', layout, size=(800,300))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        print(values)

        if event == 'Let\'s Find a Book!':
            window.close()
            book_finder()
        window.close()

def book_finder():

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text('Let\'s Find a Book!', font='Arial 14'), sg.Push()],
        [sg.Push(), sg.Text('Please fill out the fields you know below!', font='Arial, 12'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text('Book Title:', font='Arial, 12'), sg.Input(), sg.Push()],
        [sg.Push(), sg.Text('Author:', font='Arial, 12'), sg.Input(), sg.Push()],
        [sg.Push(), sg.Text('Genre:', font='Arial, 12'), sg.Input(), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button('Find Book!'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("Close Application", button_color=('black on red'))]
    ]

    window = sg.Window('Book Finder', layout, size=(500,300))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Find Book!':

            book_title = ('book title: ' + values[0]).lower()
            author = ('authors name: ' + values[1]).lower()
            genre = ('book genre: ' + values[2]).lower()

            book_to_find = open('books.txt')
            if os.path.exists('books.txt') == False:
                sg.popup(title='No Entries In Tracker', custom_text='No books are in the tracker!')
                if event == 'No Books are in the tracker!':
                    break
            else:
                with book_to_find:
                    specific = book_to_find.read().lower()
                    print(specific)
                    print(book_title, author, genre)
                    if values[0] == '':
                        if values[1] == '':
                            if values[2] == '':
                                sg.popup(title='No entries', custom_text='Please fill out the fields')
                                break
                            window.close()
                                
                    if book_title.lower() in specific.lower():
                        if author.lower() in specific.lower():
                            if genre.lower() in specific.lower():
                                book_database = open('book.database.txt', 'w+')
                                with book_database:
                                    book_database.write(book_title + "\n")
                                    book_database.write(author + "\n")
                                    book_database.write(genre + '\n')
                                    book_database.close()
                                    sg.popup(title='Finding Book', custom_text='View the book entry!')
                                    book_results(book_title, author, genre)
                                    if event == 'View the book entry!':
                                        window.close()
                    
                    else:
                        sg.popup(title='No book matches', custom_text='No book matches your search')
                        if event == 'No book matches your search':
                            window.close()

        if event == 'Close Application':
            exit()

    window.close()


def book_results(book_title, author, genre):
    
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text('Below is the book you have tracked!', font='Arial 15'), sg.Push()],
        [sg.Push(), sg.Text(book_title.title(), font='Arial 14'), sg.Push()],
        [sg.Push(), sg.Text(author.title(), font='Arial 14'), sg.Push()],
        [sg.Push(), sg.Text(genre.title(), font='Arial 14'), sg.Push()],
        [sg.VPush()],
        [sg.Button('Search for new book'), sg.Push(), sg.Button('Close Application')]
    ]

    window = sg.Window('Book Result', layout, size=(500,300))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or 'Close Application':
            break
        window.close()

        if event == 'Search for new book':
            break
    window.close()




        
if __name__ == '__main__':
    find_book()
        