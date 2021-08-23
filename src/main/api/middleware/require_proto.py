import falcon


class RequireProto(object):
    def process_request(self, req, resp):
        if req.method in ('POST', 'PUT'):
            if 'application/protobuf' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    """
                    This API only supports requests encoded as protobuf, https://developers.google.com/protocol-buffers
                    """)