import falcon

from api.resources.user.useer_mapper import user_from_proto
from api.resources.user.user_serializer import (
    get_user_response_serializer,
    post_user_request_deserializer,
    post_user_response_serializer
)
from db.data_access.user import put_user
from db.db_client import DbClient


class UserResource(object):
    auth = {
        'exempt_methods': ['POST']
    }

    @falcon.after(get_user_response_serializer)
    def on_get(self, req, resp):
        user = req.context['user']

        if user is None:
            resp.status = falcon.HTTP_404
        else:
            resp.text = user
            resp.status = falcon.HTTP_200

    @falcon.before(post_user_request_deserializer)
    @falcon.after(post_user_response_serializer)
    def on_post(self, req, resp):
        msg = req.body

        if not msg.username or not msg.email or not msg.password:
            resp.status = falcon.HTTP_400
            return

        user = user_from_proto(msg)
        put_user(self.db, user)

        resp.text = user.id

    def __init__(self, db: DbClient):
        self.db = db
