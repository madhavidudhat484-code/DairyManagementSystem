from flask import Blueprint, request, jsonify, session, redirect
from app.models import login_user, register_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"success": False, "message": "Username and password required"})

    success, result = login_user(username, password)
    if success:
        session["user"] = result
        return jsonify({"success": True, "message": "Login successful", "user": result})
    return jsonify({"success": False, "message": result})


@auth_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    username = data.get("username", "").strip()
    mobile = data.get("mobile", "").strip()
    password = data.get("password", "").strip()

    if not all([first_name, last_name, username, mobile, password]):
        return jsonify({"success": False, "message": "All fields are required"})

    if len(password) < 6:
        return jsonify(
            {"success": False, "message": "Password must be at least 6 characters"}
        )

    success, message = register_user(first_name, last_name, username, mobile, password)
    return jsonify({"success": success, "message": message})


@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True, "message": "Logged out successfully"})


@auth_bp.route("/logout")
def logout_page():
    session.clear()
    return redirect("/login")
