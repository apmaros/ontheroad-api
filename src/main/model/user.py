from dataclasses import dataclass
from typing import Optional

from common import current_time_millis, get_uuid


@dataclass
class User:
    username: str
    email: str
    password: str
    id: str = get_uuid()
    # todo serialize as int
    created_at: str = str(current_time_millis())
    updated_at: Optional[str] = None

    protected_keys = ["password", "id"]
