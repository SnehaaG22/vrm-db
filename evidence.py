from app.db import db
import uuid

class Evidence(db.Model):
    __tablename__ = "evidence"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("assessments.id"))
    file_url = db.Column(db.String(500))
