from django.db import connection
from .models import Tenant

def hostname_from_request(request):
    # split on ':' to remove port
    return request.get_host().split(':')[0].lower()

def tenant_from_request(request):
    hostname = hostname_from_request(request)
    subdomain_prefix = hostname.split('.')[0]
    return Tenant.objects.filter(subdomain_prefix=subdomain_prefix).first()

def get_tenants_map():
    return {
        "thor.polls.local": "thor",
        "potter.polls.local": "potter",
    }

def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    return get_tenants_map().get(hostname)

# def set_tenant_schema(schema):
#     with connection.cursor() as cursor:
#         cursor.execute(f"SET search_path to {schema}")


# def set_tenant_schema_for_request(request):
#     schema = tenant_schema_from_request(request)
#     set_tenant_schema(schema)
    