class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, copies):
        title, author = title.title(), author.title()
        if author not in self.books:
            self.books[author] = {}

        self.books[author][title] = self.books[author].get(title, 0) + copies
    

    def borrow_book(self, author, title):
        title, author = title.title(), author.title()
        if author not in self.books or title not in self.books[author]:
            return 'Book not available in our Library'
        if self.books[author][title] == 0:
            return 'Book not currently available in the Library'
        
        self.books[author][title] -= 1
        return f"You have successfully borrowed '{title}' by {author}"

    def return_book(self, title):
        title, author = title.title(), author.title()
        if author not in self.books:
            self.books[author] = {}

        self.books[author] = self.books[author].get(title, 0) + 1

    def get_books(self):
        return f'Available books: {self.books}'


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, library, title, author):
        response = library.borrow_book(author, title)
        if "successfully"  in response:
            self.borrowed_books.append(f"{title} by {author}")
        print(response)


    def return_book(self, library, title, author):
        if f"{title} by {author}" in self.borrowed_books:
            self.borrowed_books.remove(f"{title} by {author}")
            print(library.return_book(title, author))
        else:
            print('You do not have this book to return!')


lib = Library()
lib.add_book('Once upon a Time', 'Akeem', 12)
lib.add_book('Once upon a Time', 'Akeem', 2)
lib.add_book('Data Scientist', 'Goldmann', 1)
print(lib.get_books())
