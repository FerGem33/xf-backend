from ..utils.auth import require_api_key
from flask import Blueprint, jsonify, request
from ..db import db
from ..models import Image

images_bp = Blueprint("images", __name__)

# GET all images
@images_bp.route("/images", methods=["GET"])
def get_images():
    images = Image.query.all()
    return jsonify([
        {"id": img.image_id, "url": img.url, "entry_id": img.entry_id}
        for img in images
    ])

# GET images for a specific entry
@images_bp.route("/entries/<int:entry_id>/images", methods=["GET"])
def get_entry_images(entry_id):
    images = Image.query.filter_by(entry_id=entry_id).all()
    return jsonify([{"id": img.image_id, "url": img.url} for img in images])

# POST a new image
@images_bp.route("/images", methods=["POST"])
def add_image():
    data = request.get_json()
    image = Image(url=data["url"], entry_id=data["entry_id"])
    db.session.add(image)
    db.session.commit()
    return jsonify({"message": "Image added successfully", "id": image.image_id}), 201

# DELETE an image
@images_bp.route("/images/<int:image_id>", methods=["DELETE"])
def delete_image(image_id):
    image = Image.query.get_or_404(image_id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({"message": "Image deleted successfully"})
