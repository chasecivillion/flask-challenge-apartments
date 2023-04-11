from random import choice as rc

from app import app
from models import db, Apartment, Tenant, Lease
tenant_list = [
        Tenant(name='A', age=20),
        Tenant(name='B', age=25),
        Tenant(name='C', age=30),
        Tenant(name='D', age=35),
        Tenant(name='E', age=40),
        Tenant(name='F', age=42),
        Tenant(name='G', age=44),
        Tenant(name='H', age=50),
        Tenant(name='I', age=55),
        Tenant(name='J', age=60)
    ]

apartment_list = [
        Apartment(number=10),
        Apartment(number=20),
        Apartment(number=30),
        Apartment(number=40),
        Apartment(number=50),
        Apartment(number=60),
]

def make_apartments():
    Apartment.query.delete()

    for apartment in apartment_list:
        db.session.add(apartment)
        db.session.commit()

def make_tenants():
    Tenant.query.delete()

    for tenant in tenant_list:
        db.session.add(tenant)
        db.session.commit()

def make_leases():
    Lease.query.delete()
    lease_list = [
        Lease(rent=1000, tenant=rc(tenant_list), apartment=rc(apartment_list)),
        Lease(rent=1500, tenant=rc(tenant_list), apartment=rc(apartment_list)),
        Lease(rent=2000, tenant=rc(tenant_list), apartment=rc(apartment_list)),
        Lease(rent=2500, tenant=rc(tenant_list), apartment=rc(apartment_list)),
        Lease(rent=300, tenant=rc(tenant_list), apartment=rc(apartment_list))
    ]

    for lease in lease_list:
        db.session.add(lease)
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        make_apartments()
        make_tenants()
        make_leases()