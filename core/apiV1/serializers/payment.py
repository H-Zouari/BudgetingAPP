from rest_framework.serializers import ModelSerializer

from ...models import Payment
from .income import IncomeDetailSerializer


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentDetailSerializer(ModelSerializer):
    Income = IncomeDetailSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
