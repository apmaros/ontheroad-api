import os
from dataclasses import dataclass


@dataclass
class ServerConfig:
    host: str
    port: int


def get_server_config() -> ServerConfig:
    return ServerConfig(os.environ["API_HOST"], int(os.environ["API_PORT"]))
