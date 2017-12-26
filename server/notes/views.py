from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, \
    RetrieveModelMixin, ListModelMixin

from .models import Category, Note
from .serializers import CategorySerializer, NoteSerializer


class CategoryViewSet(
    CreateModelMixin,
    UpdateModelMixin,
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
    ListModelMixin,
    GenericViewSet,
):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    search_fields = ('title', 'body', )
    filter_fields = ('category', 'is_favourite', 'user', )
