import os
import string
from dataclasses import dataclass


@dataclass
class JwtConfig:
    secret: string
    algorithm: string
    expire_delta_hours: int


default_jwt_config = JwtConfig(
    os.environ['JWT_SECRET'],
    'HS256',
    12
)
