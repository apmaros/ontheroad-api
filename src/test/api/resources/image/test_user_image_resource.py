from unittest.mock import patch

from generated.proto import image_pb2
from generated.proto.image_pb2 import Image
from common import get_uuid, current_time_millis
from db.image_store import ImageStore
from model.user import User
from model_assert.image import assert_image_without_body
from util.api_util import get_testing_client
from util.security_util import mock_jwt_token

SECRET = mock_jwt_token()

user = User(
    username="john",
    email="john@doe.com",
    password="secret"
)

user_id = user.id
image_id = get_uuid()
created_at = current_time_millis()

mock_image = Image(
    user_id=user_id,
    name="my-mock-image",
    thumbnail_body=str.encode("image_thumbnail"),
    category='sport',
    created_at=created_at,
    id=image_id,
)

another_mock_image = Image(
    user_id=user_id,
    name="my-another-mock-image",
    thumbnail_body=str.encode("image_thumbnail"),
    category='dance',
    created_at=created_at,
    id=image_id,
)


@patch("api.resources.image.user_image_resource.get_images_by_user_id")
@patch("api.middleware.jwt_auth.get_user_by_id")
def test_get_user_image_resource(get_user_by_id_mock, get_image_by_user_id_mock):
    get_user_by_id_mock.return_value = user
    get_image_by_user_id_mock.return_value = [mock_image, another_mock_image]

    result = get_testing_client().simulate_get(
        path=f'/image',
        headers={'Authorization': f'JWT {SECRET}'}
    )

    assert result.status_code == 200
    assert get_user_by_id_mock.called
    assert get_image_by_user_id_mock.called

    proto_response = image_pb2.GetImagesResponse()
    proto_response.ParseFromString(result.content)
    images = proto_response.images

    assert_image_without_body(image=mock_image, proto_image=images[0])
    assert_image_without_body(image=another_mock_image, proto_image=images[1])


@patch("api.resources.image.user_image_resource.get_images_by_user_id")
@patch("api.middleware.jwt_auth.get_user_by_id")
def test_get_user_image_resource_when_no_auth_header_returns_401_status(
    get_user_by_id,
    get_image_by_user_id_mock
):
    get_user_by_id.return_value = user
    get_image_by_user_id_mock.return_value = [mock_image, another_mock_image]

    result = get_testing_client().simulate_get(path=f'/image')

    assert result.status_code == 401


@patch.object(ImageStore, "put", autospec=True)
@patch("api.resources.image.user_image_resource.put_image")
@patch("api.middleware.jwt_auth.get_user_by_id")
def test_post_user_image_resource(get_user_by_id, put_image_mock, image_store_put_mock):
    get_user_by_id.return_value = user

    proto_image = image_pb2.PostUserImageRequest()
    proto_image.name = "my_image"
    proto_image.category = "landscape"
    proto_image.image_body = str.encode("some_body")
    proto_image.thumbnail_body = str.encode("some_thumb_body")

    result = get_testing_client().simulate_post(
        path=f'/image',
        body=proto_image.SerializeToString(),
        headers={
            'Authorization': f'JWT {SECRET}',
            'Content-Type': 'application/protobuf',
        },
    )

    assert result.status_code == 200
    assert put_image_mock.called
    assert image_store_put_mock.called

    proto_resp = image_pb2.PostUserImageResponse()
    proto_resp.ParseFromString(result.content)

    assert proto_resp.id
