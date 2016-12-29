#!/usr/bin/python

import boto3

s3 = boto3.resource('s3')

#print out all bucket name
print("S3 Bucket Name:")
for b in s3.buckets.all():
	print(b.name)

# upload a file on s3 bucket named gauravhello
data = open('/root/hello.jpeg','rb')
s3.Bucket('gauravhello').put_object(Key='test.jpeg',Body=data)

bucket = s3.Bucket('gauravhello')
print("S3 Bucket gauravhello file names:")
for obj in bucket.objects.all():
	print(obj.key)
