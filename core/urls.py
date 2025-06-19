from django.urls import path
from .views import index
from .views import PublicEndpoint, ProtectedEndpoint, UserRegister

urlpatterns = [
    path('', index, name='index'),
    path('public/', PublicEndpoint.as_view(), name='public'),
    path('protected/', ProtectedEndpoint.as_view(), name='protected'),
    path('register/', UserRegister.as_view(), name='register'),
]