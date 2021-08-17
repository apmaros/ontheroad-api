import time
import uuid


def current_time_millis():
    return int(round(time.time() * 1000))


def get_uuid():
    return str(uuid.uuid4())


def filter_none_keys(obj_dict):
    for key in list(obj_dict):
        if obj_dict[key] is None:
            obj_dict.pop(key)

    return obj_dict
