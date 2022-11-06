from django.urls import path

from ..views.payment import (PaymentListCreateAPIView,
                              PaymentRetrieveUpdateAPIView)

app_name = 'payments'

urlpatterns = [
    path('payments/', PaymentListCreateAPIView.as_view(), name='all'),
    path('payments/<int:pk>/',
         PaymentRetrieveUpdateAPIView.as_view(),
         name='payments_details'),
]
