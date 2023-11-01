from FlaskSetup import app
import requests

@app.route('/search/<string:topic>', methods=['GET'])
def query_books_by_subject(topic):
    search_response = requests.get(f'http://127.0.0.1:5001/search/{topic}')
    return search_response.text,search_response.status_code