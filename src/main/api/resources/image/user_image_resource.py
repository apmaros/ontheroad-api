import falcon

from api.resources.image.image_mapper import image_from_proto
from api.resources.image.image_serializer import (
    get_user_images_response_serializer,
    post_user_image_request_deserializer,
    post_user_image_response_serializer,
)
from db.data_access.image import get_images_by_user_id, put_image
from db.db_client import DbClient
from db.image_store import ImageStore


class UserImageResource(object):
    @falcon.after(get_user_images_response_serializer)
    def on_get(self, req, resp):
        user = req.context["user"]

        images = get_images_by_user_id(self.db, user.id)

        resp.status = falcon.HTTP_200
        resp.text = images

    @falcon.before(post_user_image_request_deserializer)
    @falcon.after(post_user_image_response_serializer)
    def on_post(self, req, resp):
        user = req.context["user"]
        body = req.body

        if not body.name or not body.image_body:
            resp.status = falcon.HTTP_400

        image = image_from_proto(user.id, body)

        put_image(self.db, image)
        self.image_store.put(image)

        resp.status = falcon.HTTP_200
        resp.text = image

    def __init__(self, db: DbClient, image_store: ImageStore):
        self.db = db
        self.image_store = image_store
