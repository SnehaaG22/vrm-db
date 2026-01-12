from app.db import db
import uuid

class Renewal(db.Model):
    __tablename__ = "renewals"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vendor_id = db.Column(db.UUID(as_uuid=True))
    next_review_date = db.Column(db.Date)
    status = db.Column(db.Enum("DUE", "COMPLETED", name="renewal_status"))
