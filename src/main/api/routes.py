import falcon

from api.resources.image_resource import ImageResource
from api.resources.index import Index
from api.resources.login_resource import LoginResource
from api.resources.statz import Statz
from api.resources.userResource import UserResource
from api.resources.user_image_resource import UserImageResource


def set_routes(api: falcon.App, db) -> falcon.App:
    api.add_route('/', Index())
    api.add_route('/statz', Statz())
    api.add_route('/user', UserResource(db))
    api.add_route('/login', LoginResource(db))

    api.add_route('/image/{image_id}', ImageResource(db))
    api.add_route('/image', UserImageResource(db))
    return api
