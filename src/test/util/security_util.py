from datetime import datetime, timedelta
import jwt
from api.middleware.jwt_config import default_jwt_config
from common import get_uuid


def mock_jwt_token():
    jwt_config = default_jwt_config

    payload = {
        'user_id': str(get_uuid()),
        'exp': datetime.utcnow() + timedelta(
            hours=jwt_config.expire_delta_hours
        )
    }
    jwt_token = jwt.encode(
        payload,
        jwt_config.secret,
        jwt_config.algorithm
    )

    return jwt_token
