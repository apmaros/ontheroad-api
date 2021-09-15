from unittest.mock import patch

from generated.proto import user_pb2
from generated.proto.user_pb2 import PostUserRequest
from generator import make_mock_user
from model.user import User
from util.api_util import get_testing_client
from util.security_util import mock_jwt_token

SECRET = mock_jwt_token()

user = make_mock_user()


@patch("api.middleware.jwt_auth.get_user_by_id")
def test_get_user(get_user_by_id_mock):
    get_user_by_id_mock.return_value = user
    result = get_testing_client().simulate_get(
        path=f"/user", headers={"Authorization": f"JWT {SECRET}"}
    )

    assert result.status_code == 200

    proto_resp = user_pb2.GetUserResponse()
    proto_resp.ParseFromString(result.content)

    assert proto_resp.id == user.id
    assert proto_resp.username == user.username
    assert proto_resp.email == user.email


@patch("api.resources.user.user_resource.put_user")
def test_post_user(put_user_mock):
    proto_req = user_pb2.PostUserRequest()
    proto_req.username = "anotherjohn"
    proto_req.email = "anotherjohn@doe.com"
    proto_req.password = "secret"
    body = proto_req.SerializeToString()

    result = get_testing_client().simulate_post(
        path=f"/user", body=body, headers={"Content-Type": "application/protobuf"}
    )

    assert result.status_code == 200
    assert put_user_mock.called

    proto_res = user_pb2.PostUserResponse()
    proto_res.ParseFromString(result.content)

    assert proto_res.id


@patch("api.resources.user.user_resource.put_user")
def test_post_user_when_incomplete_req_returns_400_status(put_user_mock):
    proto_req = PostUserRequest()
    proto_req.email = "anotherjohn@doe.com"
    proto_req.password = "secret"
    body = proto_req.SerializeToString()

    result = get_testing_client().simulate_post(
        path=f"/user", body=body, headers={"Content-Type": "application/protobuf"}
    )

    assert result.status_code == 400
    assert not put_user_mock.called
