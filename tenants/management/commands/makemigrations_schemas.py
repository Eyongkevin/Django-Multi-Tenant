from django.core.management.commands.makemigrations import Command as MakemigrationsCommand
from django.db import connection
from ...utils import get_tenants_map
from typing import Any, Optional

# ./manage.py makemigrations_schemas
class Command(MakemigrationsCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        with connection.cursor() as cursor:
            schemas = get_tenants_map().values()
            for schema in schemas:
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
                cursor.execute(f"SET search_path to {schema}") # set connection to use this given schema
                super(Command, self).handle(*args, **options) # continue running makemigrations in that schema
                self.stdout.write(self.style.SUCCESS(f'Makemigrations successful on "{schema}" schema'))