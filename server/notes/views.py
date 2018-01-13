from django.http import Http404

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, \
    RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.response import Response

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
    search_fields = ('title', 'body', )
    filter_fields = ('category', 'is_favourite', 'user', )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if instance.user is not request.user:
            raise Http404

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class PublicNoteViewSet(
    RetrieveModelMixin,
    GenericViewSet
):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    lookup_field = 'uuid'
