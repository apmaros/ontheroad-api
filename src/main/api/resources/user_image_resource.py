import json
import falcon

from api.api_utils import get_param
from api.resources.constants import MISSING_PARAMS_ERR_MSG
from db.data_access.image import get_images_by_user_id, put_image
from db.db_client import DbClient
from db.image_store import ImageStore
from model.image import Image


class UserImageResource(object):
    def on_get(self, req, resp):
        user = req.context['user']

        images = get_images_by_user_id(self.db, user.id)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(
            list(map(lambda i: i.as_dict(), images))
        )

    def on_post(self, req, resp):
        user = req.context['user']
        name = get_param(req, 'name')
        category = get_param(req, 'category')
        body = get_param(req, 'body')

        if not name or not body:
            resp.body = json.dumps(MISSING_PARAMS_ERR_MSG)
            resp.status = falcon.HTTP_401

        image = Image(
            user_id=user.id,
            name=name,
            category=category,
            body=body
        )

        put_image(self.db, image)
        self.image_store.put(image)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(image.get_id_as_dict())

    def __init__(self, db: DbClient, image_store: ImageStore):
        self.db = db
        self.image_store = image_store
