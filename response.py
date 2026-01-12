from app.db import db
import uuid

class Response(db.Model):
    __tablename__ = "responses"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("assessments.id"))
    question_id = db.Column(db.UUID(as_uuid=True))
    answer = db.Column(db.String(255))
