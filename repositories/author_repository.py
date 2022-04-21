from db.run_sql import run_sql

from models.author import Author
from models.books import Books
import repositories.books_repository as books_repository


def save(authors):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [authors.first_name, authors.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    authors.id = id
    return authors

