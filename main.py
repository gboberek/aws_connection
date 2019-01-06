import click
import session

@click.command()
@click.option('--access_key',  help='aws access key')
@click.option('--secret_key',  help='secret key part')

def connection(access_key, secret_key):
    connection = session.authentication_class(access_key, secret_key)
    client = connection.my_session()
    blabla(client)

def blabla(session):
    s3 = session.client('s3')
    response = s3.list_buckets()
    print(response)

if __name__ == '__main__':
    connection()