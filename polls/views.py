from django.core.exceptions import PermissionDenied
from tenants.utils import tenant_from_request, set_tenant_schema_for_request
from polls.models import Poll
from polls.serializers import PollSerializer
from rest_framework import viewsets

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.select_related('created_by').all()
    serializer_class = PollSerializer

    def get_queryset(self):
        #set_tenant_schema_for_request(self.request)
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

    def destroy(self, request, *args, **kwargs):
        #set_tenant_schema_for_request(self.request)
        poll = Poll.objects.get(pk = self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not delete this poll.")
        return super().destroy(request, *args, **kwargs)
        