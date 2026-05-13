from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request, get_jwt_identity


def role_required(role):
    """Require a valid JWT and enforce a specific user role.

    Args:
        role (str): Expected role value, e.g. 'admin' or 'doctor'.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            current_user = get_jwt_identity()
            user_role = current_user.get("role")

            if user_role != role:
                return jsonify({'message': 'Access denied: insufficient role permissions'}), 403

            return fn(*args, **kwargs)

        return wrapper

    return decorator
