from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from universities.models import University, Department, Specialization


class SpecializationListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    university_name = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    logo_url = serializers.SerializerMethodField()

    @classmethod
    def get_short_description(cls, specialization):
        return specialization.get_short_description()

    @classmethod
    def get_city(cls, specialization):
        return specialization.get_city()

    @classmethod
    def get_university_name(cls, specialization):
        return specialization.get_university_name()

    @classmethod
    def get_logo_url(cls, specialization):
        return specialization.get_university_logo_url()

    class Meta:
        model = Specialization
        fields = (
            "id",
            "name",
            "university_name",
            "city",
            "short_description",
            "logo_url",
            "tags",
        )


class SpecializationDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    university_name = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    logo_url = serializers.SerializerMethodField()

    @classmethod
    def get_city(cls, specialization):
        return specialization.get_city()

    @classmethod
    def get_university_name(cls, specialization):
        return specialization.get_university_name()

    @classmethod
    def get_logo_url(cls, specialization):
        return specialization.get_university_logo_url()

    class Meta:
        model = Specialization
        fields = (
            "id",
            "name",
            "description",
            "city",
            "university_name",
            "logo_url",
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
            "logo_url",
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
            "logo_url",
            "departments",
            "tags",
        )
