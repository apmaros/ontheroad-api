import falcon

from falcon_auth import FalconAuthMiddleware
from src.main.api.middleware.jwt_auth import JwtAuth
from src.main.api.middleware.jwt_config import default_jwt_config
from src.main.api.middleware.require_proto import RequireProto
from src.main.api.routes import set_routes
from src.main.db.db_client import DbClient
from src.main.db.image_store import ImageStore


def get_api() -> falcon.App:
    db = DbClient()
    image_store = ImageStore()
    api = __build_api(db)
    return set_routes(api, db, image_store)


def __build_api(db: DbClient) -> falcon.App:
    api = falcon.App(
        middleware=[
            RequireProto(),
            FalconAuthMiddleware(
                JwtAuth(default_jwt_config, db).get_backend(),
                [],
                ['HEAD']
            )
        ]
    )
    api.req_options.auto_parse_form_urlencoded = True
    return api
