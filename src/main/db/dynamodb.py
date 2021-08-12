import os
import boto3 as boto3


# todo: extract variables into config
def build_dynamo_client():
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_session_token = os.getenv('AWS_SECRET_ACCESS_KEY')
    session = boto3.Session(
        profile_name='personal',
        region_name='eu-west-1'
    )

    return session.resource(
        'dynamodb',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_session_token,
    )