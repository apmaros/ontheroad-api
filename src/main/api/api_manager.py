import falcon
from falcon import API

from api.middleware.json_translator import JSONTranslator
from api.middleware.require_json import RequireJSON


def get_api() -> falcon.App:
    api = __build_api()
    return api


def __build_api() -> falcon.App:
    api = falcon.App(
        middleware=[
            RequireJSON(),
            JSONTranslator(),
        ]
    )
    api.req_options.auto_parse_form_urlencoded = True
    return api
