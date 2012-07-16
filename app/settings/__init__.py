import os
from app.settings.development import *

ENV_NAME = ''
if os.environ.has_key("ENV_NAME"):
    try:
        ENV_NAME = os.environ["ENV_NAME"]
        exec "from app.settings.%s import *" % ENV_NAME
    except ImportError, exp:
        pass
ENV_NAME = 'development'