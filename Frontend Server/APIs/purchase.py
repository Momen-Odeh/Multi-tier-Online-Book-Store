from FlaskSetup import app
import requests

@app.route('/purchase/<int:item_id>', methods=['POST'])
def purchase_item(item_id):
    purchase_response = requests.post(f'http://0.0.0.0:5002/purchase/{item_id}')
    return purchase_response.text,purchase_response.status_code