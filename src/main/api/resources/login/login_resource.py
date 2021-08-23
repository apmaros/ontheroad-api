import json
import logging
from datetime import datetime, timedelta
import falcon
import jwt
from api.middleware.jwt_config import default_jwt_config
from api.resources.login.login_serializer import post_login_request_deserializer, post_login_response_serializer
from api.secret import secret_is_valid
from db.data_access.user import get_user_by_email
from db.db_client import DbClient


class LoginResource(object):
    logger = logging.getLogger(__name__)

    auth = {
        'exempt_methods': ['POST']
    }

    @falcon.before(post_login_request_deserializer)
    @falcon.after(post_login_response_serializer)
    def on_post(self, req, resp):
        msg = req.body

        if msg.email is None or msg.password is None:
            resp.body = json.dumps({'error': 'One or more values is missing'})
            resp.status = falcon.HTTP_401
            return
        try:
            user = get_user_by_email(self.db, msg.email)

            if not user:
                resp.status = falcon.HTTP_404
                return

            if secret_is_valid(msg.password, user.password):
                payload = {
                    'user_id': str(user.id),
                    'exp': datetime.utcnow() + timedelta(
                        hours=self.jwt_config.expire_delta_hours
                    )
                }
                jwt_token = jwt.encode(
                    payload,
                    self.jwt_config.secret,
                    self.jwt_config.algorithm
                )

                # token = jwt.decode(jwt_token, self.jwt_config.secret, algorithms=["HS256"])
                resp.body = jwt_token
            else:
                _set_invalid_credentials(resp)
        except ValueError:
            self.logger.debug('cant verify password')
            _set_invalid_credentials(resp)

    def __init__(self, db: DbClient):
        self.jwt_config = default_jwt_config
        self.db: DbClient = db


def _set_invalid_credentials(resp):
    resp.body = json.dumps({'error': 'Credentials are not valid'})
    resp.status = falcon.HTTP_400
