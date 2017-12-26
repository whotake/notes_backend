from rest_framework.serializers import ModelSerializer

from server.notes.models import Category, Note


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description'
        )


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'created',
            'category',
            'is_favourite',
            'uuid',
            'user'
        )
        read_only_fields = ('created', 'uuid')
