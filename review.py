from app.db import db
import uuid

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id = db.Column(db.UUID(as_uuid=True))
    reviewer_id = db.Column(db.UUID(as_uuid=True))
    decision = db.Column(db.Enum("APPROVED", "REJECTED", "REMEDIATION", name="review_decision"))
