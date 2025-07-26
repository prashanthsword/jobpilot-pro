# auth/auth_guard.py

from backend.auth.utils import decode_token

def authenticate_request(token: str):
    data = decode_token(token)
    if not data:
        return {"error": "Invalid or expired token"}
    return {"username": data["username"]}


# backend/auth/auth_guard.py

from backend.auth.utils import decode_token

def authenticate_user(token: str) -> dict:
    try:
        decoded = decode_token(token)
        return decoded
    except Exception:
        return None
