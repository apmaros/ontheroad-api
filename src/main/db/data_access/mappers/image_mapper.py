from model.image import Image


def dict_to_image(image_dict: dict):
    return Image(
        user_id=image_dict["user_id"],
        name=image_dict["name"],
        thumbnail_body=image_dict["thumbnail_body"].value,
        category=image_dict["category"],
        created_at=image_dict["created_at"],
        id=image_dict["id"],
    )


def image_to_dict(image: Image):
    return image.__dict__.copy()


def image_without_body_to_dict(image: Image):
    image_dict = image.__dict__.copy()
    image_dict.pop("image_body", None)

    return image_dict
