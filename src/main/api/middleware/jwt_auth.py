from falcon_auth import JWTAuthBackend

from src.main.api.middleware.jwt_config import JwtConfig
from src.main.db.data_access.user import get_user_by_id
from src.main.db.db_client import DbClient


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
