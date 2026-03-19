from flask import Blueprint, request, jsonify
from app.models import add_customer, get_all_customers, update_customer, delete_customer

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/api/customer/add", methods=["POST"])
def add():
    data = request.get_json()
    code = data.get("code", "").strip()
    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    full_name = data.get("full_name", "").strip()
    mobile = data.get("mobile", "").strip()
    milk_type = data.get("milk_type", "").strip()
    status = data.get("status", "ON").strip()

    if not code:
        return jsonify({"success": False, "message": "Customer code is required"})

    success, message = add_customer(
        code, first_name, last_name, full_name, mobile, milk_type, status
    )
    return jsonify({"success": success, "message": message})


@customer_bp.route("/api/customer/all", methods=["GET"])
def get_all():
    success, data = get_all_customers()
    if success:
        return jsonify({"success": True, "data": data})
    return jsonify({"success": False, "message": data})


@customer_bp.route("/api/customer/update", methods=["POST"])
def update():
    data = request.get_json()
    code = data.get("code", "").strip()
    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    full_name = data.get("full_name", "").strip()
    mobile = data.get("mobile", "").strip()
    milk_type = data.get("milk_type", "").strip()
    status = data.get("status", "ON").strip()

    if not code:
        return jsonify({"success": False, "message": "Customer code is required"})

    success, message = update_customer(
        code, first_name, last_name, full_name, mobile, milk_type, status
    )
    return jsonify({"success": success, "message": message})


@customer_bp.route("/api/customer/delete", methods=["POST"])
def delete():
    data = request.get_json()
    code = data.get("code", "").strip()

    if not code:
        return jsonify({"success": False, "message": "Customer code is required"})

    success, message = delete_customer(code)
    return jsonify({"success": success, "message": message})
