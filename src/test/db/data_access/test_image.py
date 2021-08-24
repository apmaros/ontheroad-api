from unittest.mock import MagicMock
from common import get_uuid, current_time_millis
from db.data_access.image import put_image, get_image_by_id, get_images_by_user_id
from db.db_client import DbClient
from model.image import Image
from util.fakes import FakeBinary

image_id = get_uuid()
user_id = get_uuid()
created_at = str(current_time_millis())


mock_image = Image(
    user_id=user_id,
    name="my-image",
    body=str.encode("somebody"),
    thumbnail_body=str.encode("some-thumb-body"),
    category="sport",
    created_at=created_at,
    id=image_id,
)

mock_image_dic = {
    'user_id': user_id,
    'name': 'my-image',
    'thumbnail_body': FakeBinary(str.encode("some-thumb-body")),
    'category': 'sport',
    'created_at': created_at,
    'id': image_id,
}


mock_image_dic_for_db = {
    'user_id': user_id,
    'name': 'my-image',
    'thumbnail_body': str.encode("some-thumb-body"),
    'category': 'sport',
    'created_at': created_at,
    'id': image_id,
}


def test_put_image():
    db = DbClient()
    db.put_item = MagicMock()
    put_image(db, mock_image)

    db.put_item.assert_called_once_with('images', mock_image_dic_for_db)


def test_get_image_by_id():
    db = DbClient()
    db.query_index = MagicMock(return_value=[mock_image_dic])
    image = get_image_by_id(db, image_id)

    db.query_index.assert_called_once_with('images', 'images-by-id', 'id', image_id)

    # image body is not stored in DB
    mock_image.set_body(None)
    assert image == mock_image


def test_get_images_by_user_id():
    db = DbClient()
    db.query_index = MagicMock(return_value=[mock_image_dic])
    image = get_images_by_user_id(db, user_id)

    db.query_index.assert_called_once_with('images', 'images-by-user-id', 'user_id', user_id)

    # image body is not stored in DB
    mock_image.set_body(None)
    assert image == [mock_image]
