import os
from pathlib import Path

try:
    import boto3
    BOTO3_AVAILABLE = True
except ImportError:
    boto3 = None
    BOTO3_AVAILABLE = False


def create_table():
    """
    Initializes DynamoDB connection using environment variables with graceful fallback.
    """
    if not BOTO3_AVAILABLE:
        print("[AWS DynamoDB Adapter] boto3 is not installed. DynamoDB integration running in mock mode.")
        return None

    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID", "AKIAUDOF3CUUUV2HX2P4")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", "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")
    region_name = os.getenv("AWS_DEFAULT_REGION", "eu-north-1")

    try:
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        print(f"[AWS DynamoDB Adapter] Successfully configured resource in {region_name}")
        return dynamodb
    except Exception as e:
        print(f"[AWS DynamoDB Adapter] Connection notice: {e}. Running in local mock mode.")
        return None


if __name__ == '__main__':
    create_table()
