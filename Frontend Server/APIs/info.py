from FlaskSetup import app
import requests
from api_cache import get_from_cache, add_data_to_cache


@app.route('/info/<int:item_id>', methods=['GET'])
def query_book_by_item(item_id):
    data = get_from_cache(str(item_id))
    if data:
        return data, 200
    info_response = requests.get(f'localhost:5001/info/{item_id}')
    add_data_to_cache(str(item_id), info_response.text)
    return info_response.text, info_response.status_code
