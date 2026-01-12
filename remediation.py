from app.db import db
import uuid

class Remediation(db.Model):
    __tablename__ = "remediations"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id = db.Column(db.UUID(as_uuid=True))
    status = db.Column(db.Enum("OPEN", "SUBMITTED", "CLOSED", name="remediation_status"))
