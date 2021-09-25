from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from tenants.middleware.middlewares import set_db_for_router
from typing import Optional, Any

#./manage.py createsuperuser_tenant --user=? --passdword=? --email=? --database=?
class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--user', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--email', required=True)
        parser.add_argument('--database', required=False)
        
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        User = get_user_model()
        # if User.objects.exists():
        #     return 
        
        username = options['user']
        password = options['password']
        email = options['email']
        db = options['database']
    
        if db:
            from django.db import connection
            with connection.cursor() as cursor:
                set_db_for_router(db)

        User.objects.create_superuser(username=username, password=password, email=email)

        self.stdout.write(f'Local user "{username}" was created in database: {db}')


