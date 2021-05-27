import boto3
import json

AWS_KEY="<YOURAWSKEYGOESHERE>"
AWS_SECRET="<YOURAWSSECRETGOESHERE>"
AWS_REGION="<YOURAWSREGIONGOESHERE>"
BUCKET="<YOURBUCKETGOESHERE>"

s3 = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)

cors_configuration={
    'CORSRules':[
        {
            'AllowedHeaders': [
                '*'
            ],
            'AllowedMethods': [
                'PUT',
                'POST',
                'DELETE'
            ],
            'AllowedOrigins': [
                'http://www.yourrealwebsite.com'
            ],
            'ExposeHeaders': [
                'x-amz-server-side-encryption'
               
            ],
            'MaxAgeSeconds': 3000
        }
    ]
}

s3.put_bucket_cors(Bucket=BUCKET, CORSConfiguration=cors_configuration)