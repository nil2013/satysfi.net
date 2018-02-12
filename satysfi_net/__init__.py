# coding=utf-8

"""satysfi_netパッケージ初期化モジュール."""

import logging

from flask import Flask

# flask settings
app = Flask(__name__, instance_relative_config=True)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = '9sfuJnSq'
#  logger settings
app.logger.handlers.extend(logging.getLogger('gunicorn.error').handlers)
app.logger.setLevel(logging.DEBUG)
#  template settings
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from . import view # noqa
