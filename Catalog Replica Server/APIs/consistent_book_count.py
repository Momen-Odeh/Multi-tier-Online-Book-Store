from SQLiteConnection import get_db_connection
from FlaskSetup import app
from flask import jsonify

@app.route('/consistent_book_count/<int:item_id>', methods=['PUT'])
def consistent_book_count(item_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Books SET quantity = quantity - 1 WHERE id = ? AND quantity > 0', (item_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": f'update data successfully'}), 200
    except Exception as e:
        return jsonify({"message": 'error while execute in DB'}), 400