from flask_restx import Resource, Namespace

from implemented import director_service, director_schema, directors_schema

director_ns = Namespace('genres')


@director_ns.route('/')
class GenresView(Resource):

    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class GenreView(Resource):

    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
