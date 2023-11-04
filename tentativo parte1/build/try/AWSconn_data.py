import boto3


def create_table():
    dynamodb = boto3.resource('dynamodb',
                            aws_access_key_id="AKIAUDOF3CUUUV2HX2P4",
                            aws_secret_access_key="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",
                            region_name="eu-north-1")
    
create_table()

