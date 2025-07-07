from flask import Flask, jsonify
from models.user_model import db
from controllers.user_controller import user_api

import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)
app.register_blueprint(user_api)

if __name__ == "__main__":
    app.run(port=5000, debug=True)