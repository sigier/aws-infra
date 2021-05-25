import boto3
import json

AWS_KEY="<YOURAWSKEYGOESHERE>"
AWS_SECRET="<YOURAWSSECRETGOESHERE>"
AWS_REGION="<YOURAWSREGIONGOESHERE>"
BUCKET="<YOURBUCKETGOESHERE>"

s3 = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid':'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action':['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % BUCKET
    }]
}

s3.put_bucket_policy(Bucket=BUCKET, Policy=json.dumps(bucket_policy))
    

 