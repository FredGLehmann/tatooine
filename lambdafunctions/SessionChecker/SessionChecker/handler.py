import boto3

import session_checker
import config

system = session_checker.System(
    ddb=boto3.client('dynamodb', region_name=os.environ.get('SESSION_TABLE_REGION')),
    session_table=.environ.get('SESSION_TABLE'),
    cookie_name=os.environ.get('COOKIE_NAME'),
    login_url=os.environ.get('LOGIN_URL')
)

handler = system.handler
