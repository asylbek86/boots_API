
from django.contrib import admin
from django.urls import path

from boots.views import BootsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bootlist/', BootsAPIView.as_view()),
    path('api/v1/bootlist/<int:pk>', BootsAPIView.as_view()),
]
