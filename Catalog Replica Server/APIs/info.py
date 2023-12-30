from flask import jsonify
from SQLiteConnection import get_db_connection
from FlaskSetup import app

@app.route('/info/<int:item_id>', methods=['GET'])
def query_book_by_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Books WHERE id = ?', (item_id,))
    book = cursor.fetchone()
    conn.close()
    if not book:
        return jsonify({"message": 'Book not found'}), 404
    return jsonify({'book': dict(book)})