from flask import Blueprint, jsonify, request
from ..db import db
from ..models import Link

links_bp = Blueprint("links", __name__)

# GET all links
@links_bp.route("/links", methods=["GET"])
def get_links():
    links = Link.query.all()
    return jsonify([
        {"id": l.link_id, "url": l.url, "type": l.type, "idea_id": l.idea_id}
        for l in links
    ])

# GET links for a specific idea
@links_bp.route("/ideas/<int:idea_id>/links", methods=["GET"])
def get_idea_links(idea_id):
    links = Link.query.filter_by(idea_id=idea_id).all()
    return jsonify([
        {"id": l.link_id, "url": l.url, "type": l.type}
        for l in links
    ])

# POST a new link
@links_bp.route("/links", methods=["POST"])
def add_link():
    data = request.get_json()
    link = Link(url=data["url"], type=data.get("type"), idea_id=data["idea_id"])
    db.session.add(link)
    db.session.commit()
    return jsonify({"message": "Link added successfully", "id": link.link_id}), 201

# DELETE a link
@links_bp.route("/links/<int:link_id>", methods=["DELETE"])
def delete_link(link_id):
    link = Link.query.get_or_404(link_id)
    db.session.delete(link)
    db.session.commit()
    return jsonify({"message": "Link deleted successfully"})
