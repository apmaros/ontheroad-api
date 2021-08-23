from model.image import Image


def image_from_proto(user_id, proto) -> Image:
    return Image(
        user_id=user_id,
        name=proto.name,
        thumbnail_body=proto.thumbnail_body,
        body=proto.image_body,
        category=proto.category,
    )
