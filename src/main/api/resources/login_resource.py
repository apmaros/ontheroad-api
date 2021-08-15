import json
import logging
from datetime import datetime, timedelta
import falcon
import jwt
from api.middleware.jwt_config import default_jwt_config
from api.secret import secret_is_valid
from api.api_utils import get_param
from db.data_access.user import get_user_by_email
from db.db_client import DbClient


class LoginResource(object):
    logger = logging.getLogger(__name__)

    auth = {
        'exempt_methods': ['POST']
    }

    def on_post(self, req, resp):
        email = get_param(req, 'email')
        password = get_param(req, 'password')

        if email is None or password is None:
            resp.body = json.dumps({'error': 'One or more values is missing'})
            resp.status = falcon.HTTP_401
            return
        try:
            user = get_user_by_email(self.db, email)

            if not user:
                resp.status = falcon.HTTP_404
                return

            if secret_is_valid(password, user['password']):
                payload = {
                    'user_id': str(user['id']),
                    'exp': datetime.utcnow() + timedelta(
                        hours=self.jwt_config.expire_delta_hours
                    )
                }
                jwt_token = jwt.encode(
                    payload,
                    self.jwt_config.secret,
                    self.jwt_config.algorithm
                )
                token = jwt.decode(jwt_token, self.jwt_config.secret, algorithms=["HS256"])
                resp.body = json.dumps({'token': jwt_token})
            else:
                set_invalid_credentials(resp)
        except ValueError:
            self.logger.debug('cant verify password')
            set_invalid_credentials(resp)

    def __init__(self, db: DbClient):
        self.jwt_config = default_jwt_config
        self.db: DbClient = db


def set_invalid_credentials(resp):
    resp.body = json.dumps({'error': 'Credentials are not valid'})
    resp.status = falcon.HTTP_400
