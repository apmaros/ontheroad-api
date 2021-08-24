from db.data_access.mappers.user_mapper import user_to_dict, dict_to_user
from db.db_client import DbClient
from model.user import User

TABLE = 'users'


def put_user(db: DbClient, user: User):
    db.put_item(TABLE, user_to_dict(user))


def get_user_by_email(db: DbClient, email: str) -> User:
    # todo extract to config, maybe - `UsersTableConfig
    result = db.query_index(TABLE, 'users-by-email-index', 'email', email)
    return dict_to_user(result[0]) if result else None


def get_user_by_id(db: DbClient, id: str) -> User:
    result = db.query_index(TABLE, 'users-by-id-index', 'id', id)
    return dict_to_user(result[0]) if result else None
