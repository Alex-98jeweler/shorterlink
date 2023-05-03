from uuid import uuid4


def create_short_uuid():
    uuid = uuid4()
    return str(uuid[:8:])