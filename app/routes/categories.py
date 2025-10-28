from ..utils.auth import require_api_key
from flask import Blueprint, jsonify, request
from ..models import Category
from ..db import db

categories_bp = Blueprint("categories", __name__)

# GET all categories
@categories_bp.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return jsonify([
        {"id": c.category_id, "name": c.category, "color": c.color, "icon": c.icon}
        for c in categories
    ])

# POST a new category
@categories_bp.route("/categories", methods=["POST"])
def add_category():
    data = request.get_json()
    new_category = Category(
        category=data.get("name"),
        color=data.get("color"),
        icon=data.get("icon"),
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Category created successfully"}), 201

# PUT (update) a category
@categories_bp.route("/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    data = request.get_json()
    category.category = data.get("name", category.category)
    category.color = data.get("color", category.color)
    category.icon = data.get("icon", category.icon)
    db.session.commit()
    return jsonify({"message": "Category updated successfully"})

# DELETE an existing category
@categories_bp.route("/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted successfully"})
