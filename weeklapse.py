"""
A bot that uses Mastodon API to post a message once every week.
"""
from mastodon import Mastodon
import json

creds = json.load(open('creds.json'))

# Create an app
# Mastodon.create_app(
#         'weeklapse',
#         api_base_url = 'https://mastodon.sharma.io',
#         to_file = 'weeklapse_clientcred.secret'
# )

# Log in
username = creds['username']
password = creds['password']

mastodon = Mastodon(
        client_id = 'weeklapse_clientcred.secret',
        api_base_url = 'https://mastodon.sharma.io',
)

mastodon.log_in(
        username,
        password,
        to_file = 'weeklapse_usercred.secret'
)

# Post a message
mastodon.toot('From the last time you saw this message, you are one week closer to death.')
