from flask import Flask
from Routes.user_routes import user_blueprint
from Routes.request_routes import request_blueprint
import os
from flask_jwt_extended import JWTManager
import DB

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "test")
app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "test123")
jwt = JWTManager(app)
DB.get_db()

app.register_blueprint(user_blueprint)
app.register_blueprint(request_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
