from model.user import User


def user_to_dict(user: User):
    return user.__dict__


def dict_to_user(user_dict: dict):
    return User(
        username=user_dict['username'],
        email=user_dict['email'],
        password=user_dict['password'],
        id=user_dict['id'],
        created_at=user_dict.get('created_at', None),
        updated_at=user_dict.get('updated_at', None)
    )
