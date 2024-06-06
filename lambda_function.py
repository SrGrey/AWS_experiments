import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! charged from Github. Version 0.10 changing from IDE')
    }
