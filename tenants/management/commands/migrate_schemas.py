from django.core.management.commands.migrate import Command as MigrationCommand
from django.db import connection
from ...utils import get_tenants_map
from typing import Any, Optional

# ./manage.py migrate_schemas
class Command(MigrationCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        with connection.cursor() as cursor:
            schemas = get_tenants_map().values()
            for schema in schemas:
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
                cursor.execute(f"SET search_path to {schema}") # set connection to use this given schema
                super(Command, self).handle(*args, **options) # continue running all migrations
                self.stdout.write(self.style.SUCCESS(f'Successfully created "{schema}" schema'))