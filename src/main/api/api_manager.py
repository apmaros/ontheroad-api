import falcon

from falcon_auth import FalconAuthMiddleware
from api.middleware.json_translator import JSONTranslator
from api.middleware.jwt_auth import JwtAuth
from api.middleware.jwt_config import default_jwt_config
from api.middleware.require_json import RequireJSON
from api.routes import set_routes
from db.db_client import DbClient
from db.image_store import ImageStore


def get_api() -> falcon.App:
    db = DbClient()
    image_store = ImageStore()
    api = __build_api(db)
    return set_routes(api, db, image_store)


def __build_api(db: DbClient) -> falcon.App:
    api = falcon.App(
        middleware=[
            RequireJSON(),
            JSONTranslator(),
            FalconAuthMiddleware(
                JwtAuth(default_jwt_config, db).get_backend(),
                [],
                ['HEAD']
            )
        ]
    )
    api.req_options.auto_parse_form_urlencoded = True
    return api
