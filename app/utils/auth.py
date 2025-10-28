from flask import request, jsonify, current_app
from functools import wraps

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("Authorization", "")
        if key != f"Bearer {current_app.config['PRIVATE_API_KEY']}":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated
