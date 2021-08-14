import time
import uuid


def current_time_millis():
    return int(round(time.time() * 1000))


def get_uuid():
    return str(uuid.uuid4())
