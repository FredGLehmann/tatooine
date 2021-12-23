import os

import boto3

import session_manager

system = session_manager.System(
    ddb=boto3.client('dynamodb'),
    session_table='tatooinelabs-session',
    cookie_name='tatooinelabszbx',
    user_pool_client_id='okfmf59t03a2rsc0p75c89hvd',
    user_pool_domain='tatooinelabs.auth.zoubix.net',
    cloudfront_domain='tatooinelabs.zoubix.net'
)

handler = system.handler
