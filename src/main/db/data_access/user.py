from db.db_client import DbClient
from model.user import User

TABLE = 'users'


# todo return validated user object
def get_user_by_email(db: DbClient, email: str) -> User:
    # todo extract to config, maybe - `UsersTableConfig
    result = db.query_index(TABLE, 'users-by-email-index', 'email', email)
    return User.from_dict(result[0]) if result else None


def get_user_by_id(db: DbClient, id: str) -> User:
    result = db.query_index(TABLE, 'users-by-id-index', 'id', id)
    return User.from_dict(result[0]) if result else None
