from django.urls import path
from .views import CureList, CureDetail, CureDetailWithDetails

urlpatterns = [
    path('cures/', CureList.as_view(), name='cure-list'),
    path('cures/<int:id>/', CureDetail.as_view(), name='cure-detail'),
    path('cures/<int:id>/details/', CureDetailWithDetails.as_view(), name='cure-detail-with-details'),
]
