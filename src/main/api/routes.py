import falcon

from api.resources.index import Index
from api.resources.statz import Statz


def set_routes(api: falcon.App) -> falcon.App:
    api.add_route('/statz', Statz())
    api.add_route('/', Index())
    return api
