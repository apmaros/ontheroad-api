import requests

from proto import image_pb2, login_pb2, user_pb2


def build_request():
    request = image_pb2.PostUserImageRequest()
    request.name = "my_cool_image"
    request.category = "Sport"
    request.image_body = bytes("myimagebytes", encoding='utf8')
    request.thumbnail_body = bytes("myimagetumbbytes", encoding='utf8')

    return request


def send_post(url_path, data):
    r = requests.post(
        url=f'http://127.0.0.1:3000/{url_path}',
        data=data,
        headers={
            'Content-Type': 'application/protobuf',
            'Authorization': f'JWT {SECRET}'
        }
    )
    print(f"status_code={r.status_code}, content={r.content}")

    return r.content


def send_get(url_path):
    r = requests.get(
        url=f'http://127.0.0.1:3000/{url_path}',
        headers={
            'Content-Type': 'application/protobuf',
            'Authorization': f'JWT {SECRET}'
        }
    )
    print(f"status_code={r.status_code}, content={r.content}, latency={r.elapsed.total_seconds()*1000}ms")

    return r.content


def test_image():
    req = build_request()
    print(req)

    bs = req.SerializeToString()
    print(bs)

    parsed_msg = image_pb2.PostUserImageRequest()
    parsed_msg.ParseFromString(bs)
    print(parsed_msg)

    resp = send_post('image', bs)
    resp_msg = image_pb2.PostUserImageResponse()
    resp_msg.ParseFromString(resp)
    print(resp_msg.id)


def test_login():
    req = login_pb2.PostLoginRequest()
    req.password = 'secret'
    req.email = 'spike@gmail.com'

    resp = send_post('login', req.SerializeToString())
    msg = login_pb2.PostLoginResponse()
    msg.ParseFromString(resp)
    print(msg)


def test_post_user():
    req = user_pb2.PostUserRequest()
    req.username = "spike"
    req.email = "spike@gmail.com"
    req.password = "secret"

    resp = send_post('user', req.SerializeToString())
    msg = user_pb2.PostUserResponse()
    msg.ParseFromString(resp)
    print(msg)


def test_get_user():
    resp = send_get('user')
    msg = user_pb2.GetUserResponse()
    msg.ParseFromString(resp)
    print(msg)


if __name__ == '__main__':
    # test_image()
    # res = send_get("image/33d2ec88-e39e-4815-ba32-6c5fd87eb4e2")
    # msg = image_pb2.GetImageResponse()
    # msg.ParseFromString(res)
    # print(msg)
    # test_image()
    # test_login()
    # test_post_user()
    test_get_user()
