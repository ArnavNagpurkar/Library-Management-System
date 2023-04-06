# Library Management System in Python

# Welcoming the user
print("Welcome to Arnav's Library!")

# books and authors list

books = []
authors = []


# Library Class with all data

class Library:

    # Start code
    def __init__(self):
        print("1. Add book")
        print("2. View added books")
        print("3. Remove a book")
        print("4. Remove all books")
        print("5. Exit")
        self.choice = int(input("Enter choice(1/2/3/4/5): "))
        if self.choice == 1 or self.choice == 2 or self.choice == 3 or self.choice == 4 or self.choice == 5:
            pass
        else:
            print("Invalid Input\nExiting...!")
            exit()

    # adding a book
    def add_book(self):
        booknum = int(input("Enter how many books you have to add: "))
        for i in range(booknum):
            print(f"\nBook number {i + 1}\n")
            book_name = input("Enter book's name: ")
            book_name = book_name.title()
            books.append(book_name)
            author_name = input("Enter author's name: ")
            author_name = author_name.title()
            authors.append(author_name)
            print(f'Book "{book_name}" written by "{author_name}" added successfully!')

    # viewing the added books
    def view_added_books(self):
        print("Your books: \n")
        for index, book in enumerate(books):
            print(f"{index + 1}. {book}")

    # removing a book
    def remove_book(self):
        print("-----------------------------------------------------")
        print("Warning: This will only ONE book from your added list")
        print("-----------------------------------------------------")
        print("Your books: \n")
        for index, book in enumerate(books):
            print(f"{index+1}. {book}")
        removeinp = int(input("Enter the book number that you want to remove: "))
        del books[removeinp-1]
        del authors[removeinp-1]
        print("Book remove successfully!\n")

# creating a variable that contains data of library class
library = Library()

# start code execution
# automatic start due to --> __init__

# if adding a book
if library.choice == 1:
    print(
        "\nFill the information to add the books!")
    library.add_book()
    print("\n1. View added books")
    print("2. Remove a book")
    print("3. Remove all books")
    print("4. Exit")
    choice = int(input("Enter choice(1/2/3/4): "))
    # view added books
    if choice == 1:
        library.view_added_books()
    # remove a book
    elif choice == 2:
        library.remove_book()
        print("1. View added books")
        print("2. Exit")
        choice = int(input("Enter choice(1/2): "))
        if choice == 1:
            library.view_added_books()
            if books:
                print("Thanks for using Arnav's Library!\nExiting...!")
                exit()
            else:
                print("No books added!\nExiting...!")
                exit()
        elif choice == 2:
            print("Thanks for using Arnav's Library!\nExiting...!")
            exit()
    # remove all books
    elif choice == 3:
        del books
        del authors
        print("Removed all books successfully!\nThanks for using Arnav's Library!\nExiting...!")
    # exit
    elif choice == 4:
        print("Thanks for using Arnav's Library!\nExiting...!")
        exit()


# if view added books
elif library.choice == 2:
    library.view_added_books()
    if books:
        print("Thanks for using Arnav's Library!\nExiting...!")
        exit()
    else:
        print("No books added!\nExiting...!")
        exit()

# if remove a book
elif library.choice == 3:
    library.remove_book()
    print("1. View added books")
    print("2. Exit")
    choice = int(input("Enter choice(1/2): "))
    if choice == 1:
        library.view_added_books()
    elif choice == 2:
        print("Thanks for using Arnav's Library!\nExiting...!")
        exit()
    else:
        print("Invalid Input!\nExiting...!")
        exit()

# if remove all books
elif library.choice == 4:
    del books
    del authors
    print("Removed all books successfully!\nThanks for using Arnav's Library!\nExiting...!")
    exit()

# exit
elif library.choice == 5:
    print("Thanks for using Arnav's Library!\nExiting...!")
    exit()

# Invalid input
else:
    print("Invalid Input!\nExiting...!")
    exit()

# End...
