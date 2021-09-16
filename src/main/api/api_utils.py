def get_param(req, param: str):
    return req.context.doc.get(param) if param in req.context.doc else None


def get_body(req) -> bytes:
    return req.bounded_stream.read()
