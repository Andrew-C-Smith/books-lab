import pdb
from models.author import Author
from models.books import Books

import repositories.books_repository as books_repository
import repositories.author_repository as author_repository

# books_repository.delete_all()
# author_repository.delete_all()

author1 = Author("John", "Johnson")
author_repository.save(author1)

book1 = Books("Book of John", author1)
books_repository.save(book1)

# book_1 = Books("John's Book", author1)
# books_repository.save(book_1)


