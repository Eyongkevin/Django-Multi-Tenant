from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from typing import Optional, Any

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--user', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--email', required=True)
        parser.add_argument('--schema', required=False)
        
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        User = get_user_model()
        # if User.objects.exists():
        #     return 
        
        username = options['user']
        password = options['password']
        email = options['email']
        schema = options['schema']
    
        #TODO: Set tenant schema for schema
        if schema:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute(f'SET search_path to {schema}')

        User.objects.create_superuser(username=username, password=password, email=email)

        self.stdout.write(f'Local user "{username}" was created in schema: {schema}')


