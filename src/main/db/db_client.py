from dataclasses import dataclass

from db.dynamodb import build_dynamo_resource
from boto3.dynamodb.conditions import Key


class DbClient:
    client = None

    def __init__(self):
        self.client = build_dynamo_resource()

    def put_item(self, table: str, item: map):
        self.client.Table(table).put_item(Item=item)

    def get_item(self, table: str, key: map):
        result = self.client.Table(table).get_item(Key=key)
        return result['Item'] if 'Item' in result else None

    def query_index(self, table, index, key, value):
        result = self.client.Table(table).query(
            IndexName=index,
            Select="ALL_PROJECTED_ATTRIBUTES",
            ReturnConsumedCapacity="NONE",
            KeyConditionExpression=Key(key).eq(value),
        )
        return result['Items'] if 'Items' in result else None


if __name__ == '__main__':
    pass
