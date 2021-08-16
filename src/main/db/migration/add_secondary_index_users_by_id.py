from aws.services import get_dynamodb_client


def up():
    client = get_dynamodb_client()

    client.update_table(
        TableName="users",
        # Any attributes used in your new global secondary index must be declared in AttributeDefinitions
        AttributeDefinitions=[
            {
                "AttributeName": "email",
                "AttributeType": "S"
            },
            {
                "AttributeName": "password",
                "AttributeType": "S"
            },
            {
                "AttributeName": "id",
                "AttributeType": "S"
            },
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    # You need to name your index and specifically refer to it when using it for queries.
                    "IndexName": "users-by-id-index",
                    # Like the table itself, you need to specify the key schema for an index.
                    # For a global secondary index, you can use a simple or composite key schema.
                    "KeySchema": [
                        {
                            "AttributeName": "id",
                            "KeyType": "HASH"
                        }
                    ],
                    # You can choose to copy only specific attributes from the original item into the index.
                    # You might want to copy only a few attributes to save space.
                    "Projection": {
                        "ProjectionType": "INCLUDE",
                        "NonKeyAttributes": ["password", "email"]
                    },
                }
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )


if __name__ == '__main__':
    up()
