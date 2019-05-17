import os
from .infrastructure.web import create_app, ServerApplication
from .infrastructure.config import (
    DevelopmentConfig, ProductionRegistry, MemoryRegistry, Context)


def main():  # pragma: no cover
    ConfigClass = DevelopmentConfig  # type: Type[Config]
    RegistryClass = ProductionRegistry  # type: Type[Registry]

    if os.environ.get('INSTARK_DEVELOPMENT'):
        ConfigClass = DevelopmentConfig
        RegistryClass = MemoryRegistry

    config = ConfigClass()
    context = Context(config, RegistryClass(config))
    gunicorn_config = config['gunicorn']

    app = create_app(context)
    print('app>>>>>>>>', app)
    print('gunicorn_config>>>>>>', gunicorn_config)
    ServerApplication(app, gunicorn_config).run()


if __name__ == '__main__':  # pragma: no cover
    main()
