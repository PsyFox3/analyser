from flask import Flask
from flask_restful import Api
from FileHandler import GetConfig, Upload

app = Flask(__name__)
api = Api(app)

api.add_resource(Upload, '/upload')
api.add_resource(GetConfig, '/config/<client>')

# Run Server
if __name__ == '__main__':
    app.run(port=9000, debug=True)
