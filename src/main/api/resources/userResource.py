import json

import falcon

from api.api_utils import get_param
from db.db_client import DbClient
from model.user import User


class UserResource(object):
    TABLE = 'users'

    # todo add validation
    def on_get(self, req, resp):
        username = get_param(req, 'username')
        email = get_param(req, 'email')

        if username is None or email is None:
            resp.body = json.dumps({'error': 'One or more required values are missing'})
            resp.status = falcon.HTTP_401
            return

        response = self.db.get_item(table=self.TABLE, key={'username': username, 'email': email})

        if response is None:
            resp.status = falcon.HTTP_404
        else:
            resp.body = json.dumps(response)
            resp.status = falcon.HTTP_200


    def on_post(self, req, resp):
        username = get_param(req, 'username')
        email = get_param(req, 'email')

        if username is None or email is None:
            resp.body = json.dumps({'error': 'One or more required values are missing'})
            resp.status = falcon.HTTP_401
            return

        user = User(username, email)
        self.db.put_item(self.TABLE, user.__dict__)


    def __init__(self, db: DbClient):
        self.db = db


