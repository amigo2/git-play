from .models import Company
from rest_framework.viewsets import ModelViewSet

from .serializers import CompanySerializer

class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")

    
