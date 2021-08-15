from dataclasses import dataclass

from common import current_time_millis, get_uuid


@dataclass
class Image:
    user_id: str
    name: str
    category: str
    created_at: str = str(current_time_millis())
    id: str = get_uuid()

    @staticmethod
    def from_dict(image_dict):
        return Image(
            user_id=image_dict['user_id'],
            name=image_dict['name'],
            category=image_dict['category'],
            created_at=image_dict['created_at'],
            id=image_dict['id'],
        )

    def as_dict(self):
        return self.__dict__
