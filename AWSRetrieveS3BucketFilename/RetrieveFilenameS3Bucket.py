import boto3
from botocore import UNSIGNED
from botocore.client import Config

bucket_name = 'coderbytechallengesandbox'
prefix = '__cb__'

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

for page in s3.get_paginator('list_objects_v2').paginate(Bucket=bucket_name, Prefix=prefix):
    for obj in page.get('Contents', []):
        print(obj['Key'])