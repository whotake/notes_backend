from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from server.notes.permissions import NotePermission

from .models import Category, Note
from .serializers import CategorySerializer, NoteSerializer


class CategoryViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class NoteViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [NotePermission]
    search_fields = ('title', 'body')
    filter_fields = ('category', 'is_favourite', 'user')

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )


class PublicNoteViewSet(
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    lookup_field = 'uuid'
