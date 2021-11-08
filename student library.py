class Library:

    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this librart are:")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} . please keep it safe and return it within 30 days ")
            self.books.remove(bookName)
            return True
        else:
            print("sorry. this book is either not available or has already bee issued to someone else. pleas wait until the book it available")
            return False


    def returnBook(self, bookName):
        self.books.append(bookName)
        print("thanks for returning this book! hope you enjoyed it. have a great day ahead")       




class Student:
     def requestBook(self):
         self.book = input("enter the name of the book you want to borrow:")
         return self.book
         
     def returnBook(self):
         self.book = input("enter the name of the book you want to return:")
         return self.book
         

if __name__ == "__main__":
    centralLibrary = Library(["algorithms","django","clrs","python notes"])
    Student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''
        \n ==== Welcome to Central Library ====
        please choose an option:
        1. Listing all the books
        2. Request a  Book
        3. add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice:"))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(Student.requestBook()) 
        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())        
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!")

       