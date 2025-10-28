from datetime import datetime, UTC
from flask_sqlalchemy import SQLAlchemy
from .db import db

class Category(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20))
    icon = db.Column(db.String(50), nullable=False)

    entries = db.relationship("Entry", back_populates="category", cascade="all, delete")
    date_ideas = db.relationship("DateIdea", back_populates="category", cascade="all, delete")

    def __repr__(self):
        return f"<Category {self.category}>"


class Entry(db.Model):
    __tablename__ = "entries"

    entry_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"), nullable=False)

    category = db.relationship("Category", back_populates="entries")
    images = db.relationship("Image", back_populates="entry", cascade="all, delete")

    def __repr__(self):
        return f"<Entry {self.title}>"


class Image(db.Model):
    __tablename__ = "images"

    image_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    entry_id = db.Column(db.Integer, db.ForeignKey("entries.entry_id"), nullable=False)

    entry = db.relationship("Entry", back_populates="images")

    def __repr__(self):
        return f"<Image {self.url}>"


class DateIdea(db.Model):
    __tablename__ = "date_ideas"

    idea_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))

    category = db.relationship("Category", back_populates="date_ideas")
    links = db.relationship("Link", back_populates="idea", cascade="all, delete")

    def __repr__(self):
        return f"<DateIdea {self.title}>"


class Link(db.Model):
    __tablename__ = "links"

    link_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50))
    idea_id = db.Column(db.Integer, db.ForeignKey("date_ideas.idea_id"), nullable=False)

    idea = db.relationship("DateIdea", back_populates="links")

    def __repr__(self):
        return f"<Link {self.url}>"
