from typing import Optional

from src.main.services.aws.services import get_s3_client

BUCKET = "apmaros-store"


class S3Client:
    def __init__(self) -> None:
        self.client = get_s3_client()

    def put(self, key, body):
        return self.client.put_object(
            Bucket=BUCKET,
            Body=body,
            Key=key
        )

    def get(self, key) -> Optional[bytes]:
        object = self.client.get_object(
            Bucket=BUCKET,
            Key=key
        )

        if object['Body']:
            return object['Body'].read()
        else:
            return None
