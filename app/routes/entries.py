from ..utils.auth import require_api_key
from flask import Blueprint, jsonify, request
from ..db import db
from ..models import Entry, DateIdea, Link, Image

entries_bp = Blueprint("entries", __name__)

# --- Endpoints ---

# GET all journal entries
@entries_bp.route("/entries", methods=["GET"])
def get_entries():
    entries = Entry.query.all()
    result = []
    for e in entries:
        result.append({
            "id": e.entry_id,
            "title": e.title,
            "content": e.content,
            "date": e.date.isoformat(),
            "category_id": e.category_id,
            "images": [img.url for img in e.images] if hasattr(e, 'images') else []
        })
    return jsonify(result)

# POST a new journal entry
@entries_bp.route("/entries", methods=["POST"])
def add_entry():
    data = request.get_json()
    entry = Entry(
        title=data.get("title"),
        content=data.get("content"),
        date=data.get("date"),
        category_id=data.get("category_id")
    )
    db.session.add(entry)
    db.session.commit()

    # Optional: add images if provided
    for url in data.get("images", []):
        image = Image(url=url, entry_id=entry.entry_id)
        db.session.add(image)
    db.session.commit()

    return jsonify({"id": entry.entry_id, "title": entry.title}), 201


# PUT (update) an existing journal entry
@entries_bp.route("/entries/<int:entry_id>", methods=["PUT"])
def update_entry(entry_id):
    data = request.get_json()
    entry = Entry.query.get_or_404(entry_id)

    entry.title = data.get("title", entry.title)
    entry.content = data.get("content", entry.content)
    entry.date = data.get("date", entry.date)
    entry.category_id = data.get("category_id", entry.category_id)

    # Update images if provided
    if "images" in data:
        # Remove old images
        Image.query.filter_by(entry_id=entry_id).delete()
        # Add new images
        for url in data["images"]:
            db.session.add(Image(url=url, entry_id=entry_id))

    db.session.commit()
    return jsonify({"message": "Entry updated successfully"})

# DELETE a journal entry
@entries_bp.route("/entries/<int:entry_id>", methods=["DELETE"])
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({"message": "Entry deleted successfully"})
