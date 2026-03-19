from flask import Blueprint, request, jsonify
from app.models import add_rate, get_all_rates, update_rate
from datetime import date as dt_date

rate_bp = Blueprint("rate", __name__)


@rate_bp.route("/api/rate/add", methods=["POST"])
def add():
    data = request.get_json()
    milk_type = (data.get("milk_type") or data.get("type") or "").strip()
    fat = data.get("fat", "")
    snf = data.get("snf", "")
    rate = data.get("rate", "")
    date = data.get("date", str(dt_date.today()))

    if not milk_type or fat == "" or snf == "" or rate == "":
        return jsonify({"success": False, "message": "All fields are required"})

    success, result = add_rate(milk_type, fat, snf, rate, date)
    if success:
        return jsonify(
            {"success": True, "message": "Rate added successfully", "id": result}
        )
    return jsonify({"success": False, "message": result})


@rate_bp.route("/api/rate/all", methods=["GET"])
def get_all():
    success, data = get_all_rates()
    if success:
        return jsonify({"success": True, "data": data})
    return jsonify({"success": False, "message": data})


@rate_bp.route("/api/rate/update", methods=["POST"])
def update():
    data = request.get_json()
    id = data.get("id")
    milk_type = (data.get("milk_type") or data.get("type") or "").strip()
    fat = data.get("fat", "")
    snf = data.get("snf", "")
    rate = data.get("rate", "")

    if not id:
        return jsonify({"success": False, "message": "Rate ID is required"})

    success, message = update_rate(id, milk_type, fat, snf, rate)
    return jsonify({"success": success, "message": message})
