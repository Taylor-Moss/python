import boto3
import os

def delete_all_versions(bucket_name, prefix_name):
    s3 = boto3.client('s3')

    # delete all versions
    versions = s3.list_object_versions(
        Bucket=bucket_name,
        Prefix=prefix_name
    )

    # delete versions
    while True:
        for item in versions.get('Versions', []):
            s3.delete_object(
                Bucket=bucket_name,
                Key=item['Key'],
                VersionId=item['VersionId']
            )

        # delete delete markers
        for item in versions.get('DeleteMarkers',[]):
            s3.delete_object(
                Bucket=bucket_name,
                Key=item['Key'],
                VersionId=item['VersionId']
            )

        # check if there are more versions to process
        if versions.get('IsTruncated'):
            versions = s3.list_object_versions(
                Bucket=bucket_name,
                Prefix=prefix_name,
                KeyMarker=versions.get('NextKeyMarker'),
                VersionIdMarker=versions.get('NextVersionIdMarker')
            )
        else:
            break

def delete_the_bucket(bucket):
    s3 = boto3.client('s3')
    s3.delete_bucket(Bucket=bucket)

# usage
bucket = 'bucket-name'
prefix = ''
delete_all_versions(bucket, prefix)
delete_the_bucket(bucket)