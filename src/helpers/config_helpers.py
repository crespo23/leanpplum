import os


def get_base_url():

    env = os.environ.get('ENV')

    if env.lower() == 'prod':
        return 'https://www.leanplum.com'
    elif env.lower() == 'test':
        return 'https://test.leanplum.com'
    else:
        raise Exception(f'Unknown environment:{env}')

