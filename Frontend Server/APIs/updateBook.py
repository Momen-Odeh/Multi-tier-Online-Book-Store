from FlaskSetup import app
from flask import request
import requests

@app.route('/books/<int:id>', methods=['PUT'])
def updateBook(id):
    purchase_response = requests.put(f'http://localhost:5001/books/{id}',json=request.get_json())
    return purchase_response.text,purchase_response.status_code