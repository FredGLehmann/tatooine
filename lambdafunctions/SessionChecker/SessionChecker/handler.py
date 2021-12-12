import boto3
import session_checker
import config

SESSION_TABLE_REGION='eu-west-3'
SESSION_TABLE='tatooinelabs-session'
COOKIE_NAME='tatooinelabszbx'
LOGIN_URL='https://tatooinelabs.zoubix.net/_identity/login'

system = session_checker.System(
    ddb=boto3.client('dynamodb', region_name='eu-west-3'),
    session_table='tatooinelabs-session',
    cookie_name='tatooinelabszbx',
    login_url='https://tatooinelabs.zoubix.net/_identity/login'
)

handler = system.handler
