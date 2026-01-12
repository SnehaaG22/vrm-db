from app.db import db
import uuid
from sqlalchemy import UniqueConstraint

class Vendor(db.Model):
    __tablename__ = "vendors"
    __table_args__ = (UniqueConstraint("org_id", "name"),)

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("organizations.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    risk_tier = db.Column(db.Enum("LOW", "MEDIUM", "HIGH", name="risk_tiers"), nullable=False)
    status = db.Column(db.Enum("ACTIVE", "INACTIVE", name="vendor_status"), default="ACTIVE")
