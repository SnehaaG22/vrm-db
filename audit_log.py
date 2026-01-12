from app.db import db
import uuid

class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = db.Column(db.UUID(as_uuid=True))
    action = db.Column(db.String(255))
    actor_id = db.Column(db.UUID(as_uuid=True))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
