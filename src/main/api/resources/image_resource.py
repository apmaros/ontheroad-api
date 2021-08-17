import json
import falcon
from db.data_access.image import get_image_by_id
from db.db_client import DbClient
from db.image_store import ImageStore


class ImageResource(object):
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req, resp, image_id):
        image = get_image_by_id(self.db, image_id)

        if image is None:
            resp.status = falcon.HTTP_404
            return

        only_meta = bool(req.params.get("only-meta"))
        if only_meta:
            image_resp = image.as_dict()
        else:
            body = self.image_store.get_from_cdn(image)
            image_resp = image.as_dict_with_body(body)

        resp.body = json.dumps(image_resp)
        resp.status = falcon.HTTP_200

    def __init__(self, db: DbClient, image_store: ImageStore):
        self.db = db
        self.image_store = image_store
