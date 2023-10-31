from SQLiteConnection import get_db_connection
from FlaskSetup import app
from flask import jsonify

@app.route('/purchase/<int:item_id>', methods=['PUT'])
def purchase_item(item_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Books SET quantity = quantity - 1 WHERE id = ? AND quantity > 0', (item_id,))
        conn.commit()
        conn.close()
        if cursor.rowcount > 0:
            return jsonify({"message": 'Book purchase successfully'}), 200
        else:
            return jsonify({"message": 'Book not available'}), 404
    except Exception as e:
        return jsonify({"message": 'error while execute in DB'}), 400