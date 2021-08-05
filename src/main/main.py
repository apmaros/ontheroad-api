from api.api_manager import get_api
from api.config.api_config import get_server_config
from api.server import Server
from log import logger


def run():
    logger.info("Starting On The Road API 🛣")
    config = get_server_config()
    api = get_api()
    Server().start(config, api)
    logger.info("Started On The Road API")


if __name__ == '__main__':
    run()
