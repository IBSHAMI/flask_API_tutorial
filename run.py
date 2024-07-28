#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from app import create_app


if __name__ == '__main__':
    if os.environ.get('FLASK_ENV') == 'development':
        app = create_app()
        app.run(port=5000, host="0.0.0.0", use_reloader=True)
    else:
        app = create_app()
        app.run(port=5000, host="0.0.0.0", use_reloader=False)
