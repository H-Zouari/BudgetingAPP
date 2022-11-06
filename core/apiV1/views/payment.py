from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateAPIView)

from ...models import Payment
from ..serializers.payment import PaymentDetailSerializer, PaymentSerializer


class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PaymentDetailSerializer
        return super().get_serializer_class()


class PaymentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PaymentDetailSerializer
        return super().get_serializer_class()

