from app.db import db
from app.models.organization import Organization
from app.models.user import User
from app.models.vendor import Vendor
from app.models.template import Template
from app.models.assessment import Assessment
import uuid

def seed():
    org = Organization(name="Demo Corp")
    db.session.add(org)
    db.session.flush()

    admin = User(org_id=org.id, email="admin@demo.com", password_hash="admin123", role="ADMIN")
    reviewer = User(org_id=org.id, email="reviewer@demo.com", password_hash="reviewer123", role="REVIEWER")
    requester = User(org_id=org.id, email="requester@demo.com", password_hash="requester123", role="REQUESTER")

    db.session.add_all([admin, reviewer, requester])

    v1 = Vendor(org_id=org.id, name="LowRisk Vendor", risk_tier="LOW")
    v2 = Vendor(org_id=org.id, name="HighRisk Vendor", risk_tier="HIGH")

    db.session.add_all([v1, v2])

    template = Template(org_id=org.id, name="Security Assessment", version=1)
    db.session.add(template)
    db.session.flush()

    a1 = Assessment(org_id=org.id, vendor_id=v1.id, template_id=template.id, status="ASSIGNED")
    a2 = Assessment(org_id=org.id, vendor_id=v2.id, template_id=template.id, status="ASSIGNED")

    db.session.add_all([a1, a2])
    db.session.commit()
