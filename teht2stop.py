import boto3

client = boto3.client("ec2")
response = client.stop_instances(
    InstanceIds=[
         "i-08bc0d84baf937c0c",
    ],
    Hibernate=False,
    DryRun=False,
    Force=False
)