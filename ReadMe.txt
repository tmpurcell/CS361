This is a ReadMe file that detials how the microservice that I have implemented for my partner works!

This microservice allows a user to search an entry database to determine if they have previously tracked a book.

DISCLAIMER: Since we both decided to work with text files, we know that microservices need to reside in the same folder as the main program.

A. To programmatically request data, the microservice asks for a user to input the Book Title, Author, and Genre for the book they are searching for. The program 
then takes the inputed data and checks the main programs database called books.txt to see if the microservice entry matches an entry in the main database. 

B. If the microservice entry matches an entry in the main database, the values are then placed into a text file called book.database.txt. The microservice then reads this file and pulls the
information out of the text file to display to the user. 

C. UML Sequence design
    Main program -> user entry -> stored in books.txt

    Microservice -> user entry -> requests from books.txt -> user entry compared to books.txt -> if same -> books.txt information sent to book.database.txt -> microservice reads book.database.txt -> information displayed for user
                                                                                              -> if not same -> tell user that there is no entry that matches