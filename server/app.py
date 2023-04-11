from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


from models import db, Lease, Apartment, Tenant

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

migrate = Migrate( app, db )
db.init_app( app )
api = Api(app)

class Apartments(Resource):
    def get(self):
        apartments = [apartment.to_dict() for apartment in Apartment.query.all()]
        return make_response(apartments, 200)
    
    def post(self):
        data = request.get_json()
        new_apartment = Apartment(
            number = data['number']
        )
        try:
            db.session.add(new_apartment)
            db.session.commit()
        except Exception as e:
            response = {'error': f'{repr(e)}'}
            return make_response(
                response,
                422
            )
        return make_response(
            new_apartment.to_dict(),
            201
        )
    
api.add_resource(Apartments, '/apartments')
class ApartmentById(Resource):
    
    
    def patch(self, id):
        data = request.get_json()
        apartment = Apartment.query.filter_by(id=id).first()

        try:
            for key in data.keys():
                setattr(apartment, key, data[key])
            db.session.add(apartment)
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            return make_response(
                {'error': f'{repr(e)}'},
                422
            )
        return make_response(
            apartment.to_dict(),
            200
        )
        

    def delete(self, id):
        apartment = Apartment.query.filter_by(id=id).first()
        if not apartment:
            return make_response(
                {'error': 'Apartment not found'},
                404
            )
        db.session.delete(apartment)
        db.session.commit()
        return make_response(
            {'deleted?': 'delete successful'},
            200
        )


api.add_resource(ApartmentById,'/apartments/<int:id>')

if __name__ == '__main__':
    app.run( port = 3000, debug = True )