import boto3
client = boto3.client("ec2")
response = client.start_instances(
    InstanceIds=[
        'i-08bc0d84baf937c0c',
    ],
    
    DryRun=False
)