from rest_framework import viewsets
from .serializer import AppSerializer
from .models import User

# Create your views here.
class AppView(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = User.objects.all()