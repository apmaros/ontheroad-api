import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def run():
    logger.info("Starting On The Road API 🛣")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
