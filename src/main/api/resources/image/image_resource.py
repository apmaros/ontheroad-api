import falcon

from api.resources.image.image_serializer import get_image_response_serializer
from db.data_access.image import get_image_by_id
from db.db_client import DbClient
from db.image_store import ImageStore


class ImageResource(object):
    auth = {"exempt_methods": ["GET"]}

    @falcon.after(get_image_response_serializer)
    def on_get(self, req, resp, image_id):
        image = get_image_by_id(self.db, image_id)

        if image is None:
            resp.status = falcon.HTTP_404
            return

        image_body = self.image_store.get_from_cdn(image)
        image = image.set_body(image_body)

        resp.text = image
        resp.status = falcon.HTTP_200

    def __init__(self, db: DbClient, image_store: ImageStore):
        self.db = db
        self.image_store = image_store
