import boto3
import os

client = boto3.client('ecr')

repository_name = "cloud-monitoring-app-pipeline"
response = client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)

