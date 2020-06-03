from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

import Cameron.Cameron.app as frontend
from Cameron.Cameron.app import app as front


import Cameron.Cameron.minimal_example.run as survey

from flask import Flask

application = DispatcherMiddleware(front, {
    '/survey':  survey
})

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=5000,
        application=application,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True)