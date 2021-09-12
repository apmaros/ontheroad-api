import os
import boto3 as boto3


available_services = ['dynamodb', 's3']


def get_dynamodb_resource():
    return _get_resource('dynamodb')


def get_dynamodb_client():
    return _get_client('dynamodb')


def get_s3_client():
    return _get_client('s3')


def _get_resource(service_name: str):
    if service_name not in available_services:
        raise ValueError(f'Resource {service_name} is not available')

    return _get_session().resource(
        service_name=service_name,
        aws_access_key_id=_get_aws_access_key_id(),
        aws_secret_access_key=_get_secret_access_key()
    )


def _get_client(service_name: str):
    if service_name not in available_services:
        raise ValueError(f'Resource {service_name} is not available')

    return _get_session().client(
        service_name=service_name,
        aws_access_key_id=_get_aws_access_key_id(),
        aws_secret_access_key=_get_secret_access_key(),
    )


def _get_session():
    return boto3.Session(
        region_name='eu-west-1'
    )


def _get_aws_access_key_id():
    return os.getenv('AWS_ACCESS_KEY_ID')


def _get_secret_access_key():
    return os.getenv('AWS_SECRET_ACCESS_KEY')
