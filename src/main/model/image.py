from dataclasses import dataclass
from typing import Optional

from common import current_time_millis, get_uuid


@dataclass
class Image:
    user_id: str
    name: str
    thumbnail_body: Optional[bytes] = None
    image_body: Optional[bytes] = None
    category: str = "no-category"
    created_at: str = str(current_time_millis())
    id: str = get_uuid()

    def set_body(self, image_body: bytes):
        self.image_body = image_body

        return self
