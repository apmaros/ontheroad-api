from dataclasses import dataclass
from common import current_time_millis


@dataclass
class User:
    username: str
    email: str
    # todo serialize as int - problem is that int and
    created_at: str = str(current_time_millis())
    updated_at: str = None
