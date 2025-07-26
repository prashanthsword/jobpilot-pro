# auth/routes.py

from backend.auth.models import users_db, User
from backend.auth.utils import hash_password, verify_password, generate_token

def signup(username: str, password: str, email: str = None):
    if username in users_db:
        return {"error": "User already exists"}
    password_hash = hash_password(password)
    users_db[username] = User(username, password_hash, email)
    return {"message": "User created successfully"}

def login(username: str, password: str):
    user = users_db.get(username)
    if not user or not verify_password(password, user.password_hash):
        return {"error": "Invalid credentials"}
    token = generate_token(username)
    return {"token": token}
