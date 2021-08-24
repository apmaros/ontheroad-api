from typing import List

from db.data_access.mappers.image_mapper import dict_to_image, image_without_body_to_dict
from db.db_client import DbClient
from model.image import Image

TABLE = 'images'


def put_image(db: DbClient, image: Image):
    db.put_item(TABLE, image_without_body_to_dict(image))


def get_image_by_id(db: DbClient, image_id: str) -> Image:
    result = db.query_index(TABLE, 'images-by-id', 'id', image_id)
    return dict_to_image(result[0]) if result else None


# todo add pagination, or limit
def get_images_by_user_id(db: DbClient, user_id: str) -> List[Image]:
    result = db.query_index(TABLE, 'images-by-user-id', 'user_id', user_id)
    return list(map(lambda i: dict_to_image(i), result))
