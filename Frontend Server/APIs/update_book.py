from FlaskSetup import app
from flask import request
import requests
from api_cache import delete_data_from_cache
from load_balancing_catalog import round_robin


@app.route('/update/<int:item_id>', methods=['PUT'])
def update_book(item_id):
    data = request.get_json()
    info_response = requests.get(f'{round_robin()}/update/{item_id}', json=data)
    if info_response.status_code == 200:
        delete_data_from_cache(str(item_id))
        update_title = info_response.text.get("updateTitle", None)
        if update_title:
            topic_value = info_response.text.get("topic", None)
            delete_data_from_cache(str(topic_value).strip().lower())
    return info_response.text, info_response.status_code
