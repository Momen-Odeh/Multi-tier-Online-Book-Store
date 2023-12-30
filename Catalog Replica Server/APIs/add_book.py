from FlaskSetup import app
from flask import request, jsonify
from SQLiteConnection import get_db_connection
import requests
from FlaskSetup import urlReplicaServer


@app.route('/books', methods=['POST'])
def addBook():
    try:
        data = request.json
        topic = data.get('topic')
        title = data.get('title')
        price = data.get('price')
        quantity = data.get('quantity')

        if(topic and price and title and quantity):
            sql_query = 'INSERT INTO Books (topic, title, price, quantity) VALUES (?, ?, ?, ?)'
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql_query,(topic, title, price, quantity))
            
            if (data.get('be',None) is None):
                data['be'] = True
                res = requests.post(f'{urlReplicaServer}/books', json=data)
                if res.status_code !=201:
                    return {"status": "invalid request"}, 409
            conn.commit()
            cursor.execute(f"select id from Books where topic = '{topic}' and title = '{title}' and price ='{price}' and quantity = '{quantity}' ;")
            id = cursor.fetchone()[0]
            conn.close()
            return jsonify({
            "status": "insert successfully",
            "id": id
            }), 201
        return "please enter all fields", 400

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return "Bad Request", 400
