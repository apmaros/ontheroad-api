from db.dynamodb import build_dynamo_client


class DbClient:
    client = None

    def __init__(self):
        self.client = build_dynamo_client()

    def put_item(self, table: str, item: map):
        self.client.Table(table).put_item(Item=item)

    def get_item(self, table: str, key: map):
        result = self.client.Table(table).get_item(Key=key)
        return result['Item'] if 'Item' in result else None


if __name__ == '__main__':
    pass
