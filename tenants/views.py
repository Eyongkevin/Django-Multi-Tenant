from tenants.utils import tenant_from_request
from polls.models import Poll
from polls.serializers import PollSerializer
from rest_framework import viewsets



class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
