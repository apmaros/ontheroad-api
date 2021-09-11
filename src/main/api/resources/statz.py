import json
import os
import string
import falcon


def get_version() -> str:
    version = 'UNKNOWN'
    if 'APP_VERSION' in os.environ:
        version = os.environ['APP_VERSION']

    return version


class Statz(object):

    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, _, resp):
        doc = {
            'name': 'together',
            'version': get_version()
        }

        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
