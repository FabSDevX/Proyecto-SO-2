from config import Config
from app.routes import routes
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(routes)
CORS(app)


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])