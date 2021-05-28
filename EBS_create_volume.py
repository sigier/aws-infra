import boto3

AWS_KEY="<YOURAWSKEYGOESHERE>"
AWS_SECRET="<YOURAWSSECRETGOESHERE>"
AWS_REGION="<YOURAWSREGIONGOESHERE>"
AWS_AZ="<YOURAVAILABILITYZONEGOESHERE>"

client = boto3.client('ec2',region_name=AWS_REGION, aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)

response = client.create_volume(
    AvailabilityZone=AWS_AZ,
    Encrypted=False,
    Size=50,
    VolumeType='gp2'
)