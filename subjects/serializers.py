from rest_framework import serializers

from subjects.models import Subject


class SubjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            "id",
            "name",
        )
