# File: day4/my_portifolio/app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask app
app = Flask(__name__)

# --- Configuration ---
# Secret key for session management (IMPORTANT: Change this in production!)
app.config['SECRET_KEY'] = 'your_super_secret_key_here'
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirect to login page if not authenticated

# --- Database Models ---

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

# --- Flask-Login User Loader ---
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Routes ---

@app.route('/')
def home():
    return render_template('index.html')

# --- Database Initialization Function ---
def create_db():
    if not os.path.exists('dashboard.db'):
        with app.app_context():
            db.create_all()
            print("Database created successfully!")
            # Optional: Create a default admin user for testing
            if not User.query.filter_by(email='admin@example.com').first():
                admin_user = User(email='admin@example.com')
                admin_user.set_password('adminpassword') # CHANGE THIS IN PRODUCTION!
                db.session.add(admin_user)
                db.session.commit()
                print("Default admin user created: admin@example.com with password 'adminpassword'")

if __name__ == '__main__':
    create_db() # Call this to create the database and tables
    app.run(debug=True)