#!/bin/bash

export FLASK_APP=satysfi_net
export FLASK_DEBUG=1
pip install -e .
flask run
