from flask import Flask
from flask_restful import Api
from resources.Hello import Hello


app = Flask(__name__)
app.config.from_object('config')

api = Api(app)

api.add_resource(Hello, '/Hello')

if __name__ == '__main__':
    app.run()