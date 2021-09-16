import json
import falcon


class Index(object):

    auth = {"exempt_methods": ["GET"]}

    def on_get(self, _, resp):
        doc = {"name": "ontheroad-api"}

        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
