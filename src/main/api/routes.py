import falcon

from api.resources.index import Index
from api.resources.statz import Statz
from api.resources.userResource import UserResource
from db.db_client import DbClient


def set_routes(api: falcon.App) -> falcon.App:
    db = DbClient()
    api.add_route('/statz', Statz())
    api.add_route('/', Index())
    api.add_route('/user', UserResource(db))
    return api
