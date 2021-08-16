import json
import falcon

from api.api_utils import get_param
from api.resources.constants import MISSING_PARAMS_ERR_MSG
from db.data_access.image import get_images_by_user_id, put_image
from db.db_client import DbClient
from model.image import Image


class UserImageResource(object):
    def on_get(self, req, resp):
        user = req.context['user']

        images = get_images_by_user_id(self.db, user.id)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(
            list(map(lambda i: i.as_dict(), images))
        )

    def __init__(self, db: DbClient):
        self.db = db

    def on_post(self, req, resp):
        user = req.context['user']
        name = get_param(req, 'name')
        category = get_param(req, 'category')

        if not name:
            resp.body = json.dumps(MISSING_PARAMS_ERR_MSG)
            resp.status = falcon.HTTP_401

        image = Image(
            user_id=user.id,
            name=name,
            category=category,
        )

        put_image(self.db, image)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(image.as_dict())
