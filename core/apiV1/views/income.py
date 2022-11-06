from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateAPIView)

from ...models import Income
from ..serializers.income import IncomeDetailSerializer, IncomeSerializer


class IncomeListCreateAPIView(ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return IncomeDetailSerializer
        return super().get_serializer_class()


class IncomeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return IncomeDetailSerializer
        return super().get_serializer_class()
