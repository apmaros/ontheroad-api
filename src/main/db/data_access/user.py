from db.data_access.config import (
    DB_EMAIL_FIELD,
    USERS_BY_ID_INDEX,
    USERS_TABLE,
    USER_BY_EMAIL_INDEX,
    DB_ID_FIELD,
)
from db.data_access.mappers.user_mapper import user_to_dict, dict_to_user
from db.db_client import DbClient
from model.user import User


def put_user(db: DbClient, user: User):
    db.put_item(USERS_TABLE, user_to_dict(user))


def get_user_by_email(db: DbClient, email: str) -> User:
    # todo extract to config, maybe - `UsersTableConfig
    result = db.query_index(USERS_TABLE, USER_BY_EMAIL_INDEX, DB_EMAIL_FIELD, email)
    return dict_to_user(result[0]) if result else None


def get_user_by_id(db: DbClient, id: str) -> User:
    result = db.query_index(USERS_TABLE, USERS_BY_ID_INDEX, DB_ID_FIELD, id)
    return dict_to_user(result[0]) if result else None
