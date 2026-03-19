from flask import Blueprint, request, jsonify
from app.models import (
    add_collection,
    get_all_collections,
    update_collection,
    delete_collection,
)

collection_bp = Blueprint("collection", __name__)


@collection_bp.route("/api/collection/add", methods=["POST"])
def add():
    data = request.get_json()
    date = data.get("date", "").strip()
    time = data.get("time", "").strip()
    milk_type = (data.get("milk_type") or data.get("type") or "").strip()
    code = data.get("code", "").strip()
    liters = data.get("liters", "")
    fat = data.get("fat", 0)
    snf = data.get("snf", 0)
    rate = data.get("rate", "")
    total = data.get("total", "")

    if not all([date, time, milk_type, code, liters, rate]):
        return jsonify({"success": False, "message": "Please fill all required fields"})

    success, result = add_collection(
        date, time, milk_type, code, liters, fat, snf, rate, total
    )
    if success:
        return jsonify(
            {"success": True, "message": "Collection added successfully", "id": result}
        )
    return jsonify({"success": False, "message": result})


@collection_bp.route("/api/collection/all", methods=["GET"])
def get_all():
    success, data = get_all_collections()
    if success:
        return jsonify({"success": True, "data": data})
    return jsonify({"success": False, "message": data})


@collection_bp.route("/api/collection/update", methods=["POST"])
def update():
    data = request.get_json()
    id = data.get("id")
    date = data.get("date", "").strip()
    time = data.get("time", "").strip()
    milk_type = (data.get("milk_type") or data.get("type") or "").strip()
    code = data.get("code", "").strip()
    liters = data.get("liters", "")
    fat = data.get("fat", 0)
    snf = data.get("snf", 0)
    rate = data.get("rate", "")
    total = data.get("total", "")

    if not id:
        return jsonify({"success": False, "message": "Record ID is required"})

    success, message = update_collection(
        id, date, time, milk_type, code, liters, fat, snf, rate, total
    )
    return jsonify({"success": success, "message": message})


@collection_bp.route("/api/collection/delete", methods=["POST"])
def delete():
    data = request.get_json()
    id = data.get("id")

    if not id:
        return jsonify({"success": False, "message": "Record ID is required"})

    success, message = delete_collection(id)
    return jsonify({"success": success, "message": message})
