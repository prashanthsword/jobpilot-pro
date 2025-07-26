# scripts/test_auth.py
# scripts/test_auth.py

from backend.auth import utils, models, auth_guard, routes

# Simulate a signup
email = "testuser@example.com"
password = "securepass123"
hashed = utils.hash_password(password)

print("🔐 Hashed Password:", hashed)
assert utils.verify_password(password, hashed)

# Simulate token creation
token = utils.generate_token(email)
print("✅ JWT Token Created:", token)

# Decode token
decoded = utils.decode_token(token)
print("🔍 Decoded Token:", decoded)

# Simulate auth_guard
try:
    result = auth_guard.authenticate_user(token)
    print("✅ User authenticated:", result)
except Exception as e:
    print("❌ Auth failed:", e)
