from falcon_auth import JWTAuthBackend
from api.middleware.jwt_config import JwtConfig
from db.data_access.user import get_user_by_id
from db.db_client import DbClient
from model.user import User


class JwtAuth(object):
    def get_backend(self) -> JWTAuthBackend:
        return JWTAuthBackend(
            user_loader=self.__get_user,
            secret_key=self.config.secret,
            algorithm=self.config.algorithm,
            required_claims=['exp']
        )

    def __get_user(self, token):
        return get_user_by_id(self.db, token['user_id'])

    def __init__(self, config: JwtConfig, db: DbClient):
        self.db = db
        self.config = config
