from api.secret import secure_hash
from model.user import User
from proto import user_pb2


def user_from_proto(proto_user: user_pb2) -> User:
    return User(
        username=proto_user.username,
        email=proto_user.email,
        password=secure_hash(proto_user.password)
    )