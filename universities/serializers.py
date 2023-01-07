from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from universities.models import University, Department, Specialization


class SpecializationListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Specialization
        fields = (
            "id",
            "name",
            "tags",
        )


class SpecializationDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Specialization
        fields = (
            "id",
            "name",
            "description",
            "tags",
        )


class DepartmentListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "code",
            "tags",
        )


class DepartmentDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    specializations = SpecializationListSerializer(many=True)

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "code",
            "specializations",
            "tags",
        )


class UniversityListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    short_description = serializers.SerializerMethodField()

    @classmethod
    def get_short_description(cls, university):
        return university.get_short_description()

    class Meta:
        model = University
        fields = (
            "id",
            "name",
            "city",
            "short_description",
            "tags",
        )


class UniversityDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    departments = DepartmentListSerializer(many=True)

    class Meta:
        model = University
        fields = (
            "id",
            "name",
            "city",
            "description",
            "departments",
            "tags",
        )
