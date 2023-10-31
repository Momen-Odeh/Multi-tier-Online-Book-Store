from flask_cors import CORS
from FlaskSetup import app
CORS(app)


if __name__ == '__main__':
    app.run(port=5001)