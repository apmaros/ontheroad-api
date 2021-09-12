from services.aws.services import get_dynamodb_resource


def up():
    client = get_dynamodb_resource()
    client.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'email',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'username',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
        ],
        BillingMode='PAY_PER_REQUEST'
    )


if __name__ == '__main__':
    up()
