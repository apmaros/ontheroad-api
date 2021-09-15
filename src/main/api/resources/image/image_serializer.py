from api.api_utils import get_body
from generated.proto import image_pb2
from model.image import Image


def get_user_images_response_serializer(req, resp, resource):
    images = resp.text
    if not images:
        return

    proto_images = list(map(lambda image: _serialize_image(image), images))
    proto_resp = image_pb2.GetImagesResponse()
    proto_resp.images.extend(proto_images)

    resp.text = proto_resp.SerializeToString()


def post_user_image_request_deserializer(req, resp, resource, params):
    body = get_body(req)

    msg = image_pb2.PostUserImageRequest()
    msg.ParseFromString(body)

    req.body = msg


def get_image_response_serializer(req, resp, resource) -> image_pb2.GetImageResponse:
    image = resp.text
    if not image:
        return

    proto_image = _serialize_image(image)
    proto_resp = image_pb2.GetImageResponse()
    proto_resp.image.CopyFrom(proto_image)
    resp.text = proto_resp.SerializeToString()


def post_user_image_response_serializer(
    req, resp, resource
) -> image_pb2.PostUserImageResponse:
    image = resp.text

    msg = image_pb2.PostUserImageResponse()
    msg.id = image.id

    resp.text = msg.SerializeToString()


# todo remove checks
def _serialize_image(image: Image) -> image_pb2.Image:
    proto_image = image_pb2.Image()
    proto_image.user_id = image.user_id
    proto_image.name = image.name
    if image.thumbnail_body:
        proto_image.thumbnail_body = image.thumbnail_body
    if image.image_body:
        proto_image.image_body = image.image_body
    proto_image.category = image.category
    proto_image.created_at = int(image.created_at)
    proto_image.id = image.id

    return proto_image
