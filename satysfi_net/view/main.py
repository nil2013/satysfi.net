# coding=utf-8

"""メインビュー定義モジュール."""

import os
import uuid
import subprocess

from flask import render_template, request

from .. import app


@app.route('/', methods=['GET', 'POST'])
def index():
    """トップページを表示する."""

    if request.method == 'POST':
        saty = request.form['saty']
    else:
        with app.open_resource('scripts/demo/demo.saty') as f:
            saty = f.read().decode('utf-8')

    path = os.path.join(os.path.dirname(__file__), '../scripts/exec_satisfy.sh')
    p = subprocess.Popen([path, saty], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait(timeout=60)
    stdout = p.stdout.read().decode('utf-8')
    req_id = p.stderr.read().decode('utf-8')

    return render_template('index.html', saty=saty, stdout=stdout, req_id=req_id)


@app.route('/<req_id>.pdf')
def pdf(req_id):
    v = req_id.replace('-', '')
    try:
        uuid.UUID(v, version=4)
    except ValueError:
        raise Exception

    with open('/tmp/satysfi.net/demo/{:s}.pdf'.format(req_id), 'rb') as f:
        return f.read()
