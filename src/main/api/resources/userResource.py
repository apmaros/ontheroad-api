import json

import falcon

from api.api_utils import get_param
from api.resources.constants import MISSING_PARAMS_ERR_MSG
from api.secret import secure_hash
from db.data_access.user import put_user
from db.db_client import DbClient
from model.user import User


class UserResource(object):
    auth = {
        'exempt_methods': ['POST']
    }

    def on_get(self, req, resp):
        user = req.context['user']

        if user is None:
            resp.status = falcon.HTTP_404
        else:
            resp.body = json.dumps(user.as_public_dict())
            resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        username = get_param(req, 'username')
        email = get_param(req, 'email')
        password = get_param(req, 'password')

        if username is None or email is None:
            resp.body = json.dumps(MISSING_PARAMS_ERR_MSG)
            resp.status = falcon.HTTP_401
            return

        user = User(
            username=username,
            email=email,
            password=secure_hash(password)
        )
        put_user(self.db, user)

    def __init__(self, db: DbClient):
        self.db = db
