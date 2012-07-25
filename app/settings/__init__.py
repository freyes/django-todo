import os
from app.settings.development import *

ENV_NAME = ''
if os.environ.has_key("ENV_NAME"):
    try:
        ENV_NAME = os.environ.get("ENV_NAME")
        exec "from app.settings.%s import *" % ENV_NAME
    except ImportError, exp:
        pass
else:
    ENV_NAME = 'development'