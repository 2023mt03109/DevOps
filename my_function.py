import json
import boto3


def lambda_handler(event, context):
    # dynamodb = boto3.resource("dynamodb")
    # table_name = "StudentDetails"
    # table = dynamodb.Table(table_name)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Localhost!')
    }
