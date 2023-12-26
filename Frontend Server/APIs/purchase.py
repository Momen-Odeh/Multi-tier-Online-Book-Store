from FlaskSetup import app
import requests
from api_cache import delete_data_from_cache


@app.route('/purchase/<int:item_id>', methods=['POST'])
def purchase_item(item_id):
    purchase_response = requests.post(f'localhost:5002/purchase/{item_id}')
    if purchase_response.status_code == 200:
        delete_data_from_cache(str(item_id))
    return purchase_response.text, purchase_response.status_code
