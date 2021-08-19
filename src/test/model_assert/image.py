from model.image import Image
from proto import image_pb2


def assert_image(image: Image, proto_image: image_pb2.Image):
    assert_image_without_body(image=image, proto_image=proto_image)
    assert image.body == proto_image.image_body


def assert_image_without_body(image: Image, proto_image: image_pb2.Image):
    assert proto_image.user_id == image.user_id
    assert proto_image.name == image.name
    assert proto_image.thumbnail_body == image.thumbnail_body
    assert proto_image.category == image.category
    assert proto_image.created_at == image.created_at
    assert proto_image.id == image.id