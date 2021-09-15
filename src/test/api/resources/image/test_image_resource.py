from unittest.mock import patch

from generated.proto import image_pb2
from common import get_uuid, current_time_millis
from db.image_store import ImageStore
from generator import make_mock_image
from model_assert.image import assert_image
from util.api_util import get_testing_client

user_id = get_uuid()
image_id = get_uuid()
created_at = current_time_millis()

mock_image = make_mock_image(user_id=user_id, image_id=image_id, created_at=created_at)


@patch.object(ImageStore, "get_from_cdn", autospec=True)
@patch("api.resources.image.image_resource.get_image_by_id")
def test_get_image_returns_image_by_id(get_image_by_id_mock, get_from_cdn_mock):
    get_image_by_id_mock.return_value = mock_image
    get_from_cdn_mock.return_value = str.encode("my_body")

    result = get_testing_client().simulate_get(f"/image/{image_id}")
    proto_resp = image_pb2.GetImageResponse()
    proto_resp.ParseFromString(result.content)
    proto_image = proto_resp.image

    assert get_image_by_id_mock.called
    assert get_from_cdn_mock.called

    assert_image(image=mock_image, proto_image=proto_image)


@patch.object(ImageStore, "get_from_cdn", autospec=True)
@patch("api.resources.image.image_resource.get_image_by_id")
def test_image_returns_404_when_image_not_found(
    get_image_by_id_mock, get_from_cdn_mock
):
    get_image_by_id_mock.return_value = None

    result = get_testing_client().simulate_get(f"/image/{image_id}")
    assert not get_from_cdn_mock.called
    assert result.status_code == 404
