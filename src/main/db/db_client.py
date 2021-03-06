from boto3.dynamodb.conditions import Key

from services.aws.services import get_dynamodb_resource


class DbClient:
    client = None

    def __init__(self):
        self.client = get_dynamodb_resource()

    def put_item(self, table: str, item: map):
        assert self.client
        self.client.Table(table).put_item(Item=item)

    def get_item(self, table: str, key: map):
        assert self.client
        result = self.client.Table(table).get_item(Key=key)
        return result["Item"] if "Item" in result else None

    def query_index(self, table, index, key, value):
        result = self.client.Table(table).query(
            IndexName=index,
            Select="ALL_PROJECTED_ATTRIBUTES",
            ReturnConsumedCapacity="NONE",
            KeyConditionExpression=Key(key).eq(value),
        )
        return result["Items"] if "Items" in result else None
