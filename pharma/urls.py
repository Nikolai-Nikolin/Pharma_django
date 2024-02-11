from django.urls import path, include
from pharma import views

urlpatterns = [
    path("ping", views.ping, name="admin"),
    path('api/', include('pharma.api.urls')),
]
