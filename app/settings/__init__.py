import os

ENV_NAME = ''
if "ENV_NAME" in os.environ:
    try:
        ENV_NAME = os.environ.get("ENV_NAME")
        exec "from app.settings.%s import *" % ENV_NAME
    except ImportError, exp:
        pass
else:
    ENV_NAME = 'development'
    from app.settings.development import *
