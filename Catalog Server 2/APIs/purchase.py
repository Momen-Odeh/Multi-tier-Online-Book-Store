from SQLiteConnection import get_db_connection
from FlaskSetup import app
from flask import jsonify
import requests
urlReplicaServer = "http://localhost:5001"

@app.route('/purchase/<int:item_id>', methods=['PUT'])
def purchase_item(item_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Books SET quantity = quantity - 1 WHERE id = ? AND quantity > 0', (item_id,))
        conn.commit()
        if cursor.rowcount > 0:
            cursor.execute('SELECT * FROM Books WHERE id = ?', (item_id,))
            book = cursor.fetchone()
            conn.close()
            # Here request to catalog Replica to update DB
            consistent_response = requests.put(f'{urlReplicaServer}/consistent_book_count/{item_id}')
            #
            return jsonify({"message": f'bought book {book[2]}'}), 200
        else:
            return jsonify({"message": 'Book not available'}), 404
    except Exception as e:
        return jsonify({"message": 'error while execute in DB'}), 400