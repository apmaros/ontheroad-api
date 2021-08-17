from dataclasses import dataclass
from common import current_time_millis, get_uuid, filter_none_keys


@dataclass
class User:
    username: str
    email: str
    password: str
    id: str = get_uuid()
    # todo serialize as int
    created_at: str = str(current_time_millis())
    updated_at: str = None

    protected_keys = ['password', 'id']

    @staticmethod
    def from_dict(user_dict):
        return User(
            username=user_dict['username'],
            email=user_dict['email'],
            password=user_dict['password'],
            id=user_dict['id'],
            created_at=user_dict.get('created_at', None),
            updated_at=user_dict.get('updated_at', None)
        )

    def as_dict(self):
        return self.__dict__

    def as_public_dict(self):
        obj_dict = self.__dict__
        for key in self.protected_keys:
            obj_dict.pop(key)

        return filter_none_keys(obj_dict)
