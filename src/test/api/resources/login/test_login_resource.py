from unittest.mock import patch


from generated.proto.login_pb2 import PostLoginRequest, PostLoginResponse
from api.secret import secure_hash
from generator import make_mock_user
from util.api_util import get_testing_client

user = make_mock_user(password=secure_hash("secret"))


@patch("api.resources.login.login_resource.get_user_by_email")
def test_post_login_resource(get_user_by_email_mock) -> None:
    get_user_by_email_mock.return_value = user

    proto_req = PostLoginRequest()
    proto_req.email = "john@doe.com"
    proto_req.password = "secret"

    result = get_testing_client().simulate_post(
        path=f"/login",
        body=proto_req.SerializeToString(),
        headers={"Content-Type": "application/protobuf"},
    )

    assert result.status_code == 200
    assert get_user_by_email_mock.called

    proto_resp = PostLoginResponse()
    proto_resp.ParseFromString(result.content)

    assert proto_resp.token
