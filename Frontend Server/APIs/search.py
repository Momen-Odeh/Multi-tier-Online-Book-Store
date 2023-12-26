from FlaskSetup import app
import requests
from api_cache import get_from_cache, add_data_to_cache
from load_balancing_catalog import round_robin


@app.route('/search/<string:topic>', methods=['GET'])
def query_books_by_subject(topic):
    data = get_from_cache(topic)
    if data:
        return data, 200
    search_response = requests.get(f'{round_robin()}/search/{topic}')
    add_data_to_cache(topic, search_response.text)
    return search_response.text, search_response.status_code
