import json
import falcon

from api.api_utils import get_param
from api.resources.constants import MISSING_PARAMS_ERR_MSG
from db.data_access.image import get_image_by_id, get_images_by_user_id, put_image
from db.db_client import DbClient
from model.image import Image


class ImageResource(object):
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, _, resp, image_id):
        image = get_image_by_id(self.db, image_id)

        # todo fetch payload from cloudfront
        #   - path is based on the userid, category and name

        if image is None:
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(image.as_dict())

    def __init__(self, db: DbClient):
        self.db = db
