import boto3
import os 
import argparse
from datetime import datetime

def search_s3(bucket_name, prefix, start_time, end_time):
    s3 = boto3.client('s3', 
                        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
    
    datetime_obj = datetime.strptime(start_time,'%Y-%m-%d %H:%M:%S')
    year = datetime_obj.year
    # For getting  two digit numbers even if the number has one char. 
    month = datetime_obj.strftime('%m')
    day = datetime_obj.strftime('%d')
    hour = datetime_obj.strftime('%H')
    minute = datetime_obj.strftime('%M')
    second = datetime_obj.strftime('%S')

    continuationToken = ""
    file_list = []
    first_run = True
    while True:
        if continuationToken == "":
            if first_run == False:
                break
            response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
            first_run = False
        else:
            response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, ContinuationToken=continuationToken)
            continuationToken = ""

        if 'NextContinuationToken' in response:
            continuationToken = response['NextContinuationToken']

        if 'Contents' in response:
            for obj in response['Contents']:
                file_list.append(obj['Key'])
                print(obj['Key'])
        else:
            print('No objects found with the given prefix.')

    print("No: of files listed is: "+ str(len(file_list)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for searching S3 bucket by file name. Assumes environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY')
    parser.add_argument('-b', '--bucket', required=True, help='The s3 bucket that needs to be read')
    parser.add_argument('-p', '--prefix', help='Prefix to be used for searching')
    parser.add_argument('-s', '--start', default="2023-05-26 17:56:09", help='Start time in the format: YYYY-MM-DD HH:mm:ss')
    parser.add_argument('-e', '--end', default="2023-05-26 18:14:03", help='End time in the format: YYYY-MM-DD HH:mm:ss')
    args = parser.parse_args()

    print("Running with: \n")
    print("Bucket    : "+args.bucket)
    print("Prefix    : "+args.prefix)
    print("From date : "+args.start)
    print("To date   : "+args.end)
    search_s3(args.bucket, args.prefix, args.start, args.end)
