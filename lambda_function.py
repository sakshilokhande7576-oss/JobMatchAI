from app.web import app

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "JobMatchAI Lambda is working"
    }
