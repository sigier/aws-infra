import boto3
from time import sleep

AWS_KEY="<enter>"
AWS_SECRET="<enter>"
REGION="us-east-1"
AMI_ID="ami-80861296"
EC2_KEY_HANDLE="cloud"
INSTANCE_TYPE="t2.nano"
SECCGROUP_ID="<enter>"

print("Connecting to EC2...")

ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET, region_name=REGION)

print("Launching instance with AMI_ID %s, with key-pair %s, \
        instance_type %s, security_group \
        %s" % (AMI_ID,EC2_KEY_HANDLE,INSTANCE_TYPE,SECCGROUP_ID))

response = ec2.run_instances(ImageId=AMI_ID,
            KeyName=EC2_KEY_HANDLE,
            InstanceType=INSTANCE_TYPE,
            SecurityGroupIds=[SECCGROUP_ID, ],
            MinCount=1,
            MaxCount=1)
print(response)
Instance_ID=response['Instances'][0]['InstanceId']

print("Waiting for instance to be up and running")

response = ec2.describe_instances(InstanceIds=[Instance_ID])

status=response['Reservations'][0]['Instances'][0]['State']['Name']

print("Status: "+str(status))

while status=='pending':
    sleep(10)
    response=ec2.describe_instances(InstanceIds=[Instance_ID])
    status=response['Reservations'][0]['Instances'][0]['State']['Name']
    print("Status: "+str(status))

if status=='running':
    response=ec2.describe_instances(InstanceIds=[Instance_ID])
    print("\nInstance is now running. Instance details are:")
    print("Instance Type: "+ \
        str(response['Reservations'][0][Instances][0]['InstanceType']))
    print("Instance State: "+ \
        str(response['Reservations'][0][Instances][0]['State']['Name']))
    print("Instance Launch Time: "+ \
        str(response['Reservations'][0][Instances][0]['LaunchTime']))
    print("Instance Public DNS: "+ \
        str(response['Reservations'][0][Instances][0]['PublicDnsName']))
    print("Instance Private DNS: "+ \
        str(response['Reservations'][0][Instances][0]['PrivateDnsName']))
    print("Instance IP: "+ \
        str(response['Reservations'][0][Instances][0]['PublicIpAddress']))
    print("Instance Private IP: "+ \
        str(response['Reservations'][0][Instances][0]['PrivateIpAddress']))
