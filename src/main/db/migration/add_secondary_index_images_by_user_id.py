from aws.services import get_dynamodb_client


def up():
    client = get_dynamodb_client()

    client.update_table(
        TableName="images",
        # Any attributes used in your new global secondary index must be declared in AttributeDefinitions
        AttributeDefinitions=[
            {
                "AttributeName": "user_id",
                "AttributeType": "S"
            }
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    # You need to name your index and specifically refer to it when using it for queries.
                    "IndexName": "images-by-user-id",
                    # Like the table itself, you need to specify the key schema for an index.
                    # For a global secondary index, you can use a simple or composite key schema.
                    "KeySchema": [
                        {
                            "AttributeName": "user_id",
                            "KeyType": "HASH"
                        }
                    ],
                    # You can choose to copy only specific attributes from the original item into the index.
                    # You might want to copy only a few attributes to save space.
                    "Projection": {
                        "ProjectionType": "ALL",
                    },
                }
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )


if __name__ == '__main__':
    up()
