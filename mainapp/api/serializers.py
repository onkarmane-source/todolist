from rest_framework import serializers
# from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from mainapp.models import *
from django.utils import timezone
import json


class TagSerializer(serializers.ModelSerializer):

    name = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Tag
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    # tags = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field="name"
    )
    update_tags = serializers.ListField(
        child=serializers.CharField(max_length=30), write_only=True, required=False)

    class Meta:
        lookup_field = 'id'
        model = ToDoList
        fields = ("id", "title", "description", "due_date", "update_tags",
                  "tags", "status", "timestamp")
        read_only_fields = ('id', 'timestamp')

    def create(self, validated_data):
        print("incomming data", validated_data)
        tag_names = []
        tags = []
        if "update_tags" in validated_data:
            tag_names = validated_data.pop('update_tags')
        if "tags" in validated_data:
            tags = validated_data.pop("tags")
        instance = super().create(validated_data)

        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        instance.tags.set(tags)
        return instance

    def update(self, instance, validated_data):
        print("incomming data", validated_data)
        tag_names = []
        if "update_tags" in validated_data:
            tag_names = validated_data.pop('update_tags')

        instance = super().update(instance, validated_data)
        user = self.context['request'].user
        tags = validated_data['tags']
        for name in tag_names:
            # tag, created = Tag.objects.get_or_create(name=name, defaults={'created_by': user})
            tag, created = Tag.objects.get_or_create(name=name)

            tags.append(tag)
        instance.tags.set(tags)
        return instance
