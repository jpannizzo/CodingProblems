class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} - {self.genre}"

    def search_by_author(books, author_lookup):
        for book in books:
            if author_lookup.lower() == book.author.lower():
                return book
        return "Book not found when searching for Author"

    def search_by_title(books, title_lookup):
        for book in books:
            if title_lookup.lower() in book.title.lower():
                return book
        return "Book not found when searching for Title"

    def binary_search_title(books, title_lookup):
        start = 0
        stop = len(books)-1

        while start <= stop:
            counter = (start + stop) // 2
            if title_lookup.lower() == books[counter].title.lower():
                return books[counter]
            elif title_lookup.lower() < books[counter].title.lower():
                stop = counter - 1
            else:
                start = counter + 1

        return "Book not found during binary search"

books = [
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book("To Kill a Mockingbird", "Herper Lee", "Fiction"),
    Book("1984", "George Orwell", "Fiction"),
    Book("Pride and Prejudice", "Jane Austen", "Romance"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
]

sorted_books = [
    Book("1984", "George Orwell", "Fiction"),
    Book("Pride and Prejudice", "Jane Austen", "Romance"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book("To Kill a Mockingbird", "Herper Lee", "Fiction"),
]

results = [
    Book.search_by_author(books, "Jane Austen"), # test author search
    Book.search_by_title(books, "To Kill a Mockingbird"), # test title search
    Book.search_by_title(books, "98"), # test partial title search
    Book.search_by_author(books, "Frank"), # test author not found
    Book.search_by_title(books, "Frank"), # test partial title search
    Book.binary_search_title(sorted_books, "The Great Gatsby"), # test binary search
    Book.binary_search_title(sorted_books, "James and the Giant Peach") # test binary search not found
]

for result in results:
    print(result)