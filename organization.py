from app.db import db
import uuid

class Organization(db.Model):
    __tablename__ = "organizations"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
