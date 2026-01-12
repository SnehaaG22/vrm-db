from app.db import db
import uuid
from sqlalchemy import UniqueConstraint

class Template(db.Model):
    __tablename__ = "templates"
    __table_args__ = (UniqueConstraint("org_id", "name", "version"),)

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("organizations.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    version = db.Column(db.Integer, nullable=False)
