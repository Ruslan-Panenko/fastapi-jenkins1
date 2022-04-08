import json
import os

with open(os.path.join(os.path.dirname(__file__), 'secrets.json'), 'r') as f:
    secrets = json.loads(f.read())


def get_secret(setting):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f'Set the {setting} secret variable'
        raise error_msg


DB_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
    get_secret('DB_USER'),
    get_secret('DB_PASSWORD'),
    get_secret('DB_HOST'),
    get_secret('DB_PORT'),
    get_secret('DB_NAME'),
)