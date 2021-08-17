import base64
from dataclasses import dataclass

from common import current_time_millis, get_uuid, filter_none_keys


@dataclass
class Image:
    user_id: str
    name: str
    body: str = None
    category: str = "no-category"
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
        return filter_none_keys(self.__dict__)

    def as_dict_with_body(self, body: bytes):
        obj_dict = filter_none_keys(self.__dict__)
        b = base64.b64encode(body)
        obj_dict['body'] = b.decode('ascii')

        return obj_dict

    def as_dict_without_body(self):
        obj_dict = filter_none_keys(self.__dict__.copy())
        obj_dict.pop('body', None)

        return obj_dict

    def get_id_as_dict(self):
        return {'id': self.id}
