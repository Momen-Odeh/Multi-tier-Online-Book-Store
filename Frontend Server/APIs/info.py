from FlaskSetup import app
import requests

@app.route('/info/<int:item_id>', methods=['GET'])
def query_book_by_item(item_id):
    info_response = requests.get(f'http://0.0.0.0:5001/info/{item_id}')
    return info_response.text,info_response.status_code