from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# override djoser's user registration serializer
class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "photo",
            "Country",
            "role",
            "password",
            "last_login",
        )


# override user details serializer
class UserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "photo",
            "Country",
            "role",
            "password",
            "last_login",
            "is_active",
        )
