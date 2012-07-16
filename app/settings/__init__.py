import os
from app.settings.development import *

ENV_NAME = ''
if os.environ.has_key("ENV_NAME"):
    try:
        exec "from app.settings.%s import *" % os.environ["ENV_NAME"]
        ENV_NAME = os.environ["ENV_NAME"]
    except ImportError, exp:
        pass