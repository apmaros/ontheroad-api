import json

import falcon

from api.api_utils import get_param
from api.secret import secure_hash
from db.data_access.user import get_user_by_email
from db.db_client import DbClient
from model.user import User


class UserResource(object):
    TABLE = 'users'
    REQUIRED_PARAMETERS_MISSING_ERR_MSG = {'error': 'One or more required values are missing'}

    # todo add validation
    def on_get(self, req, resp):
        email = get_param(req, 'email')

        if email is None:
            resp.body = json.dumps(self.REQUIRED_PARAMETERS_MISSING_ERR_MSG)
            resp.status = falcon.HTTP_401
            return

        response = get_user_by_email(self.db, email)

        if response is None:
            resp.status = falcon.HTTP_404
        else:
            resp.body = json.dumps(response)
            resp.status = falcon.HTTP_200


    def on_post(self, req, resp):
        username = get_param(req, 'username')
        email = get_param(req, 'email')
        password = get_param(req, 'password')

        if username is None or email is None:
            resp.body = json.dumps(self.REQUIRED_PARAMETERS_MISSING_ERR_MSG)
            resp.status = falcon.HTTP_401
            return

        user = User(
            username=username,
            email=email,
            password=secure_hash(password)
        )
        self.db.put_item(self.TABLE, user.__dict__)


    def __init__(self, db: DbClient):
        self.db = db


