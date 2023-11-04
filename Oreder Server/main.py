from flask_cors import CORS
from FlaskSetup import app
CORS(app)
import requests
from SQLiteConnection import get_db_connection

@app.route('/purchase/<int:item_id>', methods=['POST'])
def purchase_item(item_id):
    purchase_response = requests.put(f'http://catalog:5001/purchase/{item_id}')
    status = 'success' if purchase_response.status_code==200 else 'failed'
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO Orders (bookId, status) VALUES (?, ?)"
    data = (item_id, status)
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()
    connection.close()

    return purchase_response.text, purchase_response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
