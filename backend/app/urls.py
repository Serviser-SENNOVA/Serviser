from django.urls import path, include
from rest_framework import routers
from app import views

#Registration of uurl
router = routers.SimpleRouter()
router.register(r'users', views.AppView, 'users')

urlpatterns = [
    path('api/v1/', include(router.urls))
]
