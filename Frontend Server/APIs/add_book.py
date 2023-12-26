from FlaskSetup import app
from flask import request
import requests
from api_cache import delete_data_from_cache
from load_balancing_catalog import round_robin


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    info_response = requests.post(f'{round_robin()}/books', json=data)
    if info_response.status_code == 200:
        delete_data_from_cache(str(data['topic']).strip().lower())
    return info_response.text, info_response.status_code
