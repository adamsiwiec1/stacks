import boto3
import json


def do_test():
    json_object = {
        "this is jsos": "yes it is"   
    }
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
    s3.create_bucket(Bucket='testbucket')
    s3.put_object(Body=json.dumps(json_object), Bucket='testbucket', Key='object.json')
    obj = s3.get_object(Bucket='testbucket', Key='object.json')
    print("my object in s3:\n" + str(obj['Body'].read()))

if __name__ == '__main__':
    do_test()