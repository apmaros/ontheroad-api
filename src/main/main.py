from log import logger

from api.api_manager import get_api
from api.config.api_config import get_server_config
from api.server import Server

APP_NAME = "On The Road API"


def run():
    logger.info(f"Starting  {APP_NAME} 🛣")
    config = get_server_config()
    api = get_api()
    Server().start(config, api)
    logger.info(f"Started {APP_NAME} API")


if __name__ == "__main__":
    run()
