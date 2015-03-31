import os
from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "blog.config.DevelopmentConfig")
# blog.config refers to the path \blog\config
app.config.from_object(config_path)

from . import views
from . import filters
from . import login