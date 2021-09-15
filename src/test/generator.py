from common import get_uuid, current_time_millis
from model.image import Image
from model.user import User


def make_mock_user(
    user_id: str = get_uuid(), created_at=str(current_time_millis()), password="secret"
) -> User:
    return User(
        username="john",
        email="john@doe.com",
        password=password,
        id=user_id,
        created_at=created_at,
        updated_at=None,
    )


def make_mock_image(
    user_id: str = get_uuid(),
    image_id: str = get_uuid(),
    created_at=str(current_time_millis()),
) -> Image:
    return Image(
        user_id=user_id,
        name="my-image",
        image_body=str.encode("somebody"),
        thumbnail_body=str.encode("some-thumb-body"),
        category="sport",
        created_at=created_at,
        id=image_id,
    )
