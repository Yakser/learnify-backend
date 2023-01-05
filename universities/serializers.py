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
            "description",
        )


class SpecializationDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Specialization
        fields = (
            "id",
            "name",
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

    class Meta:
        model = University
        fields = (
            "id",
            "name",
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
            "description",
            "departments",
            "tags",
        )
