import names
import random

from flask import(
    Flask,
    Request,
    render_template,
    Response
)

from flask.app import Flask as FlaskApp

from models.book import Book

app: Flask = Flask(__name__)
books: list[Book] = []

@app.route('/')
def main_page():
    return render_template(
        template_name_or_list="index.html",
        ctx_books=enumerate(books)
    )

@app.route('/<id>')
def current_book(id: str):
    try:
        return render_template(
            template_name_or_list="book.html",
            ctx_book=books[int(id)]
        )
    except:
        return "Ошибка"

if __name__ == '__main__':
    for _ in range(20):
        book = Book(
            name=names.get_first_name(),
            description=names.get_last_name(),
            price=round(
                random.random() * 1000 + 1000,
                2
            ),
            list_count=random.randint(100, 300),
            rate_list=[
                random.randint(1, 5)
            ]
        )
        
        books.append(book)

    app.run(
        port=8080,
        debug=True
    )