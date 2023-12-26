from flask import jsonify
from SQLiteConnection import get_db_connection
from FlaskSetup import app

@app.route('/search/<string:topic>', methods=['GET'])
def query_books_by_subject(topic):
    conn = get_db_connection()
    cursor = conn.cursor()
    # cursor.execute("SELECT id, title, topic FROM Books WHERE lower(topic) LIKE ?", ('%' + topic.lower() + '%',))
    cursor.execute('SELECT id, title FROM Books WHERE lower(topic) = ?', (topic.lower(),))
    books = cursor.fetchall()
    conn.close()
    if not books:
        return jsonify({"message": 'No books found for the specified topic'}), 404
    return jsonify({'books': [{'id': book[0], 'title': book[1]} for book in books]})