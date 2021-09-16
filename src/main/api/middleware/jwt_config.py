import os
from dataclasses import dataclass


@dataclass
class JwtConfig:
    secret: str
    algorithm: str
    expire_delta_hours: int


default_jwt_config = JwtConfig(os.environ["JWT_SECRET"], "HS256", 12)
