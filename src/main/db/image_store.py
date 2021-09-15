from model.image import Image
from services.cdn.cdn_client import CdnClient
from services.s3.s3_client import S3Client


class ImageStore:
    def __init__(self):
        self.s3 = S3Client()
        self.cdn = CdnClient()

    def put(self, image: Image):
        if not image.image_body:
            raise ValueError("Can not store image without body")

        self.s3.put(_get_key(image), image.image_body)

    def get(self, image: Image):
        return self.s3.get(_get_key(image))

    def get_from_cdn(self, image: Image):
        return self.cdn.get_object(_get_key(image))


def _get_key(image: Image) -> str:
    return f"{image.user_id}/{image.category}/{image.id}.{image.name}"
