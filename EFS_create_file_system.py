import boto3
import json

AWS_KEY="<YOURAWSKEYGOESHERE>"
AWS_SECRET="<YOURAWSSECRETGOESHERE>"
AWS_REGION="<YOURAWSREGIONGOESHERE>"


client = boto3.client('efs', region_name=AWS_REGION,
    aws_access_key_id=AWS_KEY, 
    aws_secret_access_key=AWS_SECRET)

response = client.create_file_system(
    CreationToken='myfs',
    PerformanceMode='generalPurpose',
    Encrypted=False,
    ThroughputMode='bursting'
)
