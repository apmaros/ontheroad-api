import falcon

from api.middleware.json_translator import JSONTranslator
from api.middleware.require_json import RequireJSON
from api.routes import set_routes


def get_api() -> falcon.App:
    api = __build_api()
    return set_routes(api)


def __build_api() -> falcon.App:
    api = falcon.App(
        middleware=[
            RequireJSON(),
            JSONTranslator(),
        ]
    )
    api.req_options.auto_parse_form_urlencoded = True
    return api
