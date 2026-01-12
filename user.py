from app.db import db
import uuid
from sqlalchemy import UniqueConstraint

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("org_id", "email"),)

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("organizations.id"), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum("ADMIN", "REVIEWER", "REQUESTER", name="user_roles"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
