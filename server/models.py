from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


# - A tenant has many apartments and has many leases
# - An apartment has many tenants and has many leases
# - A lease belongs to an apartment and belongs to a tenant


class Lease(db.Model, SerializerMixin):
    __tablename__ = 'leases'

    serialize_rules = ('-apartment','-tenant')

    id = db.Column(db.Integer, primary_key=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.id'))
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    rent = db.Column(db.Float, nullable=False)

    apartment = db.relationship('Apartment', back_populates='leases')
    tenant = db.relationship('Tenant', back_populates='leases')

class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'

    serialize_rules = ('-leases','-apartments')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    leases = db.relationship('Lease', back_populates='tenant')
    apartments = association_proxy('leases', 'apartment')

    @validates('age')
    def validate_age(self, key, age):
        if age < 18:
            raise ValueError('must be 18 or older')
        return age


class Apartment(db.Model, SerializerMixin):
    __tablename__ = 'apartments'

    serialize_rules = ('-leases','tenants')

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)

    leases = db.relationship('Lease', back_populates='apartment')
    tenants = association_proxy('leases', 'tenant')

