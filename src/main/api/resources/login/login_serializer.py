from api.api_utils import get_body
from proto import login_pb2


def post_login_request_deserializer(req, resp, resource, params):
    body = get_body(req)

    msg = login_pb2.PostLoginRequest()
    msg.ParseFromString(body)

    req.body = msg


def post_login_response_serializer(req, resp, resource):
    token = resp.text

    if not token:
        return

    msg = login_pb2.PostLoginResponse()
    msg.token = token
    resp.text = msg.SerializeToString()
