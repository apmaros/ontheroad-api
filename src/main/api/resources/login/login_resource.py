import logging
from datetime import datetime, timedelta
import falcon
import jwt

from src.main.api.middleware.jwt_config import default_jwt_config
from src.main.api.resources.login.login_serializer import post_login_request_deserializer, \
    post_login_response_serializer
from src.main.api.secret import secret_is_valid
from src.main.db.data_access.user import get_user_by_email
from src.main.db.db_client import DbClient


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
            resp.status = falcon.HTTP_400
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
                resp.text = jwt_token
            else:
                resp.status = falcon.HTTP_400
        except ValueError:
            self.logger.debug('cant verify password')
            resp.status = falcon.HTTP_400

    def __init__(self, db: DbClient):
        self.jwt_config = default_jwt_config
        self.db: DbClient = db

