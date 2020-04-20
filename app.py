from flask import Flask
from flask_restful import Resource, Api
from sekolah import Sekolah
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tai kucing lah'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

api.add_resource(Sekolah , '/api/v1/testSekolah')

if __name__ == '__main__':
    app.run(debug=True)