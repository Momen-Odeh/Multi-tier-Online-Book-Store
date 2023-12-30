from FlaskSetup import app
from flask import request,jsonify
from SQLiteConnection import get_db_connection
import requests
from FlaskSetup import urlReplicaServer


@app.route('/books/<int:id>', methods=['PUT'])
def updateBook(id):
    try:
        data = request.json
        title = data.get('title')
        price = data.get('price')
        quantity = data.get('quantity')
        if(id is None):
            return "please enter book id", 400
        title_update = []
        val = []
        updateTitle = False
        if (title is not None):
            title_update.append('title')
            val.append(title)
            updateTitle=True
        if (price is not None):
            title_update.append('price')
            val.append(price)
        if (quantity is not None):
            title_update.append('quantity')
            val.append(quantity)
        if(len(val) == 0):
            return "invalid input data", 400
        set_clause = ', '.join([f'{column} = ?' for column in title_update])
        sql_query = f'UPDATE Books SET {set_clause} WHERE id = ?'
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query, val + [id])

        if(data.get('be',None) is None):
            data['be'] = True
            res = requests.put(f'{urlReplicaServer}/books/{id}', json=data)
            if res.status_code !=200:
                    return {"status": "invalid request"}, 409
        conn.commit()
        cursor.execute(f"select topic from Books where id = '{id}' ;")
        topic = cursor.fetchone()[0]
        conn.close()
        return jsonify({
        "status": "update successfully",
        "id": id,
        "topic": topic,
        "updateTitle": updateTitle
        }), 200

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return "Bad Request", 400
