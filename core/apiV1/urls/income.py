from django.urls import path

from ..views.income import (IncomeListCreateAPIView,
                            IncomeRetrieveUpdateAPIView,)

app_name = 'income'

urlpatterns = [
    path('income/', IncomeListCreateAPIView.as_view(), name='all'),
    path('income/<int:pk>/',
         IncomeRetrieveUpdateAPIView.as_view(),
         name='income_details'),
]
