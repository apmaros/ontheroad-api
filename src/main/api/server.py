from wsgiref import simple_server

from api.config.api_config import ServerConfig
from log import logger


class Server:
    server = simple_server

    def start(self, config: ServerConfig, api):
        logger.info(f'starting server listening on {config.host}:{config.port}')

        httpd = self.server.make_server(
            config.host,
            config.port,
            api
        )

        # seems it creates only one worker
        httpd.serve_forever()
        logger.info("server started")
