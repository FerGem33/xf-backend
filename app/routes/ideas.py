from flask import Blueprint, jsonify, request
from ..db import db
from ..models import Entry, DateIdea, Link, Image

ideas_bp = Blueprint("ideas", __name__)

# --- Endpoints ---

# GET all date ideas
@ideas_bp.route("/ideas", methods=["GET"])
def get_ideas():
    ideas = DateIdea.query.all()
    result = []
    for idea in ideas:
        result.append({
            "id": idea.idea_id,
            "title": idea.title,
            "content": idea.content,
            "category_id": idea.category_id,
            "links": [{"url": link.url, "type": link.type} for link in idea.links] if hasattr(idea, "links") else []
        })
    return jsonify(result)

# POST a new date idea
@ideas_bp.route("/ideas", methods=["POST"])
def add_idea():
    data = request.get_json()
    idea = DateIdea(
        title=data.get("title"),
        content=data.get("content"),
        category_id=data.get("category_id")
    )
    db.session.add(idea)
    db.session.commit()

    # Optional: add links if provided
    for link_data in data.get("links", []):
        link = Link(url=link_data["url"], type=link_data.get("type"), idea_id=idea.idea_id)
        db.session.add(link)
    db.session.commit()

    return jsonify({"id": idea.idea_id, "title": idea.title}), 201

# POST (update) an existing date idea
@ideas_bp.route("/ideas/<int:idea_id>", methods=["PUT"])
def update_idea(idea_id):
    data = request.get_json()
    idea = DateIdea.query.get_or_404(idea_id)

    idea.title = data.get("title", idea.title)
    idea.content = data.get("content", idea.content)
    idea.category_id = data.get("category_id", idea.category_id)

    # Update links if provided
    if "links" in data:
        # Remove old links
        Link.query.filter_by(idea_id=idea_id).delete()
        # Add new links
        for link_data in data["links"]:
            db.session.add(Link(url=link_data["url"], type=link_data.get("type"), idea_id=idea_id))

    db.session.commit()
    return jsonify({"message": "Date idea updated successfully"})


# DELETE a date idea
@ideas_bp.route("/ideas/<int:idea_id>", methods=["DELETE"])
def delete_idea(idea_id):
    idea = DateIdea.query.get_or_404(idea_id)
    db.session.delete(idea)
    db.session.commit()
    return jsonify({"message": "Date idea deleted successfully"})
