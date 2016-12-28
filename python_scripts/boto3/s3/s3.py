#!/usr/bin/python

import boto3

s3 = boto3.resource('s3')

for b in s3.buckets.all():
	print(b.name)

data = open('/root/hello.jpeg','rb')
s3.Bucket('gauravhello').put_object(Key='test.jpeg',Body=data)
