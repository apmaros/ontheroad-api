import requests


class CdnClient:
    CDN_URL = "https://dfupbai80fwui.cloudfront.net"

    def get_object(self, path: str) -> bytes:
        """
        :param path to the object stored in CDN
        :return: returns fetched object in bytes
        """
        resp = requests.get(f"{self.CDN_URL}/{path}")

        return resp.content
