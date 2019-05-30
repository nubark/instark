import sys
from argparse import ArgumentParser, Namespace
from injectark import Injectark
from ..core import Config
from ..web import create_app, ServerApplication

class Cli:
    def __init__(self, config: Config, resolver: Injectark) -> None:
        self.config = config
        self.resolver = resolver
        self.registry = resolver

        args = self.parse()
        args.func(args)
    
    def parse(self) -> Namespace:
        parser = ArgumentParser('Instark')
        subparsers = parser.add_subparsers()

        # Setup
        # setup_parser = subparsers.add_parser(
        #     'setup', help='Prepare system environment.')
        # setup_parser.set_defaults(func=self.setup)

        # Provision
        provision_parser = subparsers.add_parser(
            'provision', help='Provision new tenants.')
        provision_parser.add_argument('data')
        provision_parser.set_defaults(func=self.provision)

        # Serve
        serve_parser = subparsers.add_parser(
            'serve', help='Start HTTP server.')
        serve_parser.set_defaults(func=self.serve)

        if len(sys.argv[1:]) == 0:
            parser.print_help()
            parser.exit()

        return parser.parse_args()
    
    # def setup(self, args: Namespace) -> None:
    #     print('...SETUP:::', args)
    #     print('...END SETUP:::')

    def provision(self, args: Namespace) -> None:
        print('...PROVISION::::')
        tenant_supplier = self.resolver['TenantSupplier']
        tenant_dict = {'name': args.name} # test 1
        tenant_dict = json.loads(args.data) # test 2
        tenant_supplier.create_tenant(tenant_dict)
        print('...END PROVISION::::')
    
    def serve(self, args: Namespace) -> None:
        print('...SERVE:::', args)
        app = create_app(self.config, self.resolver)
        gunicorn_config = self.config['gunicorn']
        ServerApplication(app, gunicorn_config).run()
