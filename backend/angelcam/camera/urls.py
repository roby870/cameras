from django.urls import path
from .views import SharedCamerasView


urlpatterns = [
    path('shared-cameras/', SharedCamerasView.as_view(), name='shared-cameras'),
    path('shared-cameras/<str:next_url>/', SharedCamerasView.as_view(), name='shared-cameras'),
]