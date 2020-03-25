import aiohttp_cors
from pathlib import Path
from jinja2 import FileSystemLoader
from aiohttp import web
from aiohttp_jinja2 import setup
#from flask import Flask
#from flask_cors import CORS
from injectark import Injectark
from .api import create_api
from .generators import setup_generators
from middleware import middlewares
#from .errors import register_error_handler

def create_app(config, injector: Injectark) -> web.Application:
    app = web.Application(middlewares=middlewares(injector))
    templates = str(Path(__file__).parent / 'templates')
    setup(app, loader=FileSystemLoader(templates))
    setup_generators(app)
    create_api(app, injector)
    enable_cors(app)

    return app


async def run_app(app: web.Application, port=4321) -> None:
    await web._run_app(app, port=port)


def enable_cors(app: web.Application) -> None:
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)
        
"""def create_app(config, resolver: Injectark) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.update(config['flask'])
    register_error_handler(app)

    create_api(app, resolver)

    return app
"""