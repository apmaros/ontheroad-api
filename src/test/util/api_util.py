from falcon import testing

from api.api_manager import get_api


def get_testing_client():
    return testing.TestClient(get_api())
