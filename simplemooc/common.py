site_env = get_env_variable('SITE_ENV')
if site_env:
    if site_env == 'staging':
        from .staging import *
    elif site_env == 'production':
        from .production import *
