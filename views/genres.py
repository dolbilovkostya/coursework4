from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from parsers import page_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        filters = page_parser.parse_args()
        genres = genre_service.get_all(filters)
        res = GenreSchema(many=True).dump(genres)
        return res, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
