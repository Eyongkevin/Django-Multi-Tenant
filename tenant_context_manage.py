#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
Run with:
    python tenant_context_manage.py <schema-name> createsuperuser

"""

import sys
from django.db import connection
import os


def main():
    """Run administrative tasks in a per schema mode."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
        from tenants.middleware.middlewares import set_db_for_router
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    args = sys.argv
    db = args[1]
    with connection.cursor() as cursor:
        set_db_for_router(db)
        del args[1]
        #execute_from_command_line(args)


if __name__ == '__main__':
    main()