from unittest.mock import MagicMock
from common import get_uuid, current_time_millis
from db.data_access.user import get_user_by_email, get_user_by_id, put_user
from db.db_client import DbClient
from generator import make_mock_user


user_id = get_uuid()
created_at = str(current_time_millis())

mock_user = make_mock_user(user_id, created_at=created_at)

mock_user_dict = {
    "username": "john",
    "email": "john@doe.com",
    "password": "secret",
    "id": user_id,
    "created_at": created_at,
    "updated_at": None,
}


def test_put_user():
    db = DbClient()
    db.put_item = MagicMock()
    put_user(db, mock_user)

    db.put_item.assert_called_once_with("users", mock_user_dict)


def test_get_user_by_email():
    db = DbClient()
    db.query_index = MagicMock(return_value=[mock_user_dict])
    user = get_user_by_email(db, "john@doe.com")

    db.query_index.assert_called_once_with(
        "users", "users-by-email-index", "email", "john@doe.com"
    )
    assert user == mock_user


def test_get_user_by_id():
    db = DbClient()
    db.query_index = MagicMock(return_value=[mock_user_dict])
    user = get_user_by_id(db, user_id)

    db.query_index.assert_called_once_with("users", "users-by-id-index", "id", user_id)
    assert user == mock_user
