from rest_framework import routers

from server.notes.views import CategoryViewSet, NoteViewSet, PublicNoteViewSet

router = routers.SimpleRouter()

router.register(
    'category',
    CategoryViewSet,
    base_name='category',
)
router.register(
    'note',
    NoteViewSet,
    base_name='note',
)
router.register(
    'public-note',
    PublicNoteViewSet,
    base_name='public-note',
)

urlpatterns = []
urlpatterns += router.urls
