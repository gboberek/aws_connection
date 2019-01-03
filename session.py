import boto3

# class boto3.session.Session(aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, region_name=None, botocore_session=None, profile_name=None)

class authentication_class(object)
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key


    def my_session(self):
        s = boto3.session.Session(aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        return s

    def blabla(self):
        klient = s.client('s3')
        response = klient.list_buckets()
        print(response)