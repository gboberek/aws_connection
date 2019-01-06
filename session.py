import boto3

class authentication_class(object):
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def my_session(self):
        print('connecting')
        s = boto3.session.Session(aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key, region_name='eu-central-1')
        return s

