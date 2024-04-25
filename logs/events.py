import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="logs/events.log"
)

def log_info(msg: str) -> None:
    logging.info(msg)

def log_error(msg: str) -> None:
    logging.error(msg)

def log_warning(msg: str) -> None:
    logging.warning(msg)
