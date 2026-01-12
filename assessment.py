from app.db import db
import uuid

class Assessment(db.Model):
    __tablename__ = "assessments"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = db.Column(db.UUID(as_uuid=True), nullable=False)
    vendor_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("vendors.id"))
    template_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("templates.id"))
    status = db.Column(db.Enum(
        "ASSIGNED", "IN_PROGRESS", "SUBMITTED", "REVIEWED", "APPROVED", "REJECTED",
        name="assessment_status"
    ), nullable=False)
