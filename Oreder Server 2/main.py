from flask_cors import CORS
from FlaskSetup import app
from flask import jsonify, request
CORS(app)
import requests
from SQLiteConnection import get_db_connection

catalog_servers = ['http://localhost:5001', 'http://localhost:5003']


def round_robin():
    global catalog_servers
    server = catalog_servers.pop(0)
    catalog_servers.append(server)
    return server


urlReplicaServer = "http://localhost:5002"
@app.route('/purchase/<int:item_id>', methods=['POST'])
def purchase_item(item_id):
    purchase_response = requests.put(f'{round_robin()}/purchase/{item_id}')
    status = 'success' if purchase_response.status_code==200 else 'failed'
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO Orders (bookId, status) VALUES (?, ?)"
    data = (item_id, status)
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()
    connection.close()
    consistent_response = requests.post(url=f'{urlReplicaServer}/consistent_record', json={"bookId": item_id, "status": status})

    return purchase_response.text, purchase_response.status_code

@app.route('/consistent_record', methods=['POST'])
def consistent_record():
    try:
        data = request.get_json()
        connection = get_db_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO Orders (bookId, status) VALUES (?, ?)"
        print(data.get("bookId"), "******", data.get("status"))
        data = (data.get("bookId"), data.get("status"))
        cursor.execute(sql, data)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": f'update data successfully'}), 200
    except Exception as e:
        return jsonify({"message": 'error while execute in DB'}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
