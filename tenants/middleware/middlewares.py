import contextvars
from tenants.utils import tenant_db_from_request

THREAD_LOCAL_DB = contextvars.ContextVar('db', default=None)

class TenantMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_request(request)
        THREAD_LOCAL_DB.set(db)
        response = self.get_response(request)
        return response 

def get_current_db_name():
    return THREAD_LOCAL_DB.get()

def set_db_for_router(db):
    THREAD_LOCAL_DB.set(db)