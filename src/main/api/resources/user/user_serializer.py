from api.api_utils import get_body
from model.user import User
from proto import user_pb2


def get_user_response_serializer(req, resp, resource):
    user: User = resp.text

    msg = user_pb2.GetUserResponse()
    msg.id = user.id
    msg.username = user.username
    msg.email = user.email

    resp.text = msg.SerializeToString()


def post_user_request_deserializer(req, resp, resource, params):
    body = get_body(req)

    msg = user_pb2.PostUserRequest()
    msg.ParseFromString(body)

    req.body = msg


def post_user_response_serializer(req, resp, resource):
    user_id = resp.text
    if not user_id:
        return

    msg = user_pb2.GetUserResponse()
    msg.id = user_id

    resp.text = msg.SerializeToString()
