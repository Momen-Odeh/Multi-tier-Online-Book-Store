from SQLiteConnection import get_db_connection
from FlaskSetup import app
from flask import jsonify, request

@app.route('/books/update-quantity/<int:item_id>', methods=['PUT'])
def update_quantity_item(item_id):
    try:
        data = request.get_json()
        quantity = data['quantity']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Books SET quantity = ? WHERE id = ?', (quantity, item_id))
        conn.commit()
        conn.close()
        return jsonify({"message": 'quantity updated successfully'}), 200
    except Exception as e:
        return jsonify({"message": 'error while execute in DB'}), 400