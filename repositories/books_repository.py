from db.run_sql import run_sql

from models.author import Author
from models.books import Books
import repositories.author_repository as author_repository


def save(books):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *" #SQL
    values = [books.title, books.author.id] #python
    results = run_sql(sql, values)
    id = results[0]['id']
    books.id = id
    return books

def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)