from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    achievements = serializers.SerializerMethodField()
    favorite_subjects = serializers.SerializerMethodField()
    about = serializers.SerializerMethodField()

    def get_achievements(self, user):
        return user.profile.achievements

    def get_favorite_subjects(self, user):
        return user.profile.favorite_subjects

    def get_about(self, user):
        return user.profile.about

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "achievements",
            "favorite_subjects",
            "about",
        )


class UserListSerializer(serializers.ModelSerializer):
    achievements = serializers.SerializerMethodField()

    def get_achievements(self, user):
        return user.profile.achievements

    def create(self, validated_data):
        user = User(**validated_data)

        user.set_password(validated_data["password"])
        user.save()

        return user

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "achievements",
            # "favorite_subjects",
            # "about",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "achievements": {"write_only": True},
            # "favorite_subjects": {"write_only": True},
            # "about": {"write_only": True},
        }
