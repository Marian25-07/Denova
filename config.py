import os

class Config:
    # Flask secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

    # JWT secret key for token signing
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your-jwt-secret-key-here'

    # MongoDB Atlas connection URI
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://Kamilo:1234KL@denova.kdqkau6.mongodb.net/?appName=Denova'

    # SQLite database path
    SQLITE_DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'app.db')

    # Ensure the instance directory exists
    if not os.path.exists(os.path.dirname(SQLITE_DATABASE)):
        os.makedirs(os.path.dirname(SQLITE_DATABASE))
        