from typing import Dict
from pathlib import Path
from migrark import sql_migrate
from ..common import SchemaConnection, TenantSupplier
from .migration_supplier import MigrationSupplier


class SchemaMigrationSupplier(MigrationSupplier):
    def __init__(self, zones: Dict[str, str],
                 tenant_supplier: TenantSupplier) -> None:
        self.zones = zones
        self.tenant_supplier = tenant_supplier
        self.template_schema = '__template__'
        self.migrations_path = str(
            (Path(__file__).parent.parent.parent / 'data' /
             'sql' / 'migrations').absolute())

        print("&"*120)
        print("migrations_path    ", self.migrations_path)
        print("&"*120)

    def migrate(self, tenant: str = '', version: str = '') -> None:
        domain = []
        if tenant:
            domain = [('slug', 'in', tenant.lower().split(','))]

        version = version or '999'

        tenants = self.tenant_supplier.search_tenants(domain)

        for zone, dsn in self.zones.items():
            schemas = [self.template_schema]
            for tenant_dict in tenants:
                if (tenant_dict['zone'] or 'default') == zone:
                    schemas.append(tenant_dict['slug'])
                # tenant_zone: str = tenant_dict['zone'] or 'default'

                # if tenant_zone == zone:
                #     schemas.append(tenant_dict['slug'])

            connection = SchemaConnection(dsn)
            context = {'placeholder': '%s'}
            for schema in schemas:
                sql_migrate(connection, self.migrations_path,
                            schema, context=context,
                            target_version=version)
