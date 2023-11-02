from flask_cors import CORS
from FlaskSetup import app
CORS(app)
import requests

@app.route('/purchase/<int:item_id>', methods=['POST'])
def purchase_item(item_id):
    purchase_response = requests.put(f'http://catalog:5001/purchase/{item_id}')
    return purchase_response.text, purchase_response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
