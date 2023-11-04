from SQLiteConnection import get_db_connection
from FlaskSetup import app
from flask import jsonify, request

@app.route('/books/update-cost/<int:item_id>', methods=['PUT'])
def update_cost_item(item_id):
    try:
        data = request.get_json()
        cost = data['cost']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Books SET price = ? WHERE id = ?', (cost, item_id))
        conn.commit()
        conn.close()
        return jsonify({"message": 'cost updated successfully'}), 200
    except Exception as e:
        return jsonify({"message": 'error while execute in DB'}), 400