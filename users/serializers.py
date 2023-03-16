from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_superuser'
        ]

        read_only_fields = ['is_superuser']
        
        extra_kwargs = {
            "username": {
                "required": True,
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
            "email": {
                "required": True,
                "validators": [UniqueValidator(queryset=User.objects.all())],
            },
            'password': {'write_only': True}
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(raw_password=instance.password)
        instance.save()

        return instance