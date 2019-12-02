from flask import Flask
from flask_restful import Api
from FileHandler import get_config, upload

app = Flask(__name__)
api = Api(app)

api.add_resource(upload, '/upload')
api.add_resource(get_config, '/config/<client>')

# Run Server
if __name__ == '__main__':
    app.run(port=9000, debug=True)