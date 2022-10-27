
import boto3

s3 = boto3.client('s3')
response = s3.download_file('mikko-s3bucket-awssdk', 'uusi_lista.txt','mikon_awslista.txt')
