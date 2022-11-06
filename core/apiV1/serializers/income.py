from rest_framework.serializers import ModelSerializer,SerializerMethodField

from ...models import Income
from .account import AccountSerializer

class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class IncomeDetailSerializer(ModelSerializer):
    source = AccountSerializer()
    class Meta:
        model = Income
        fields = '__all__'
