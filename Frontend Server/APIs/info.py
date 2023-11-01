from FlaskSetup import app
import requests

@app.route('/info/<int:item_id>', methods=['GET'])
def query_book_by_item(item_id):
    order_response = requests.get(f'http://127.0.0.1:5000/info/{item_id}')
    return order_response.text,order_response.status_code