from flask_cors import CORS
from FlaskSetup import app
from APIs.info import query_book_by_item
from APIs.search import query_books_by_subject
from APIs.purchase import purchase_item
CORS(app)

if __name__ == '__main__':
    app.run(port=5001)