import boto3

AWS_KEY="<YOURAWSKEYGOESHERE>"
AWS_SECRET="<YOURAWSSECRETGOESHERE>"
AWS_REGION="<YOURAWSREGIONGOESHERE>"
 

client = boto3.client('ec2',region_name=AWS_REGION, aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)

volume=client.Volume('vol-0788f9eefe22cfa')
snapshot = volume.create_snapshot(
    Description='snapshotEBS'
)