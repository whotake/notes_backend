from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from server.notes.views import CategoryViewSet, NoteViewSet, PublicNoteViewSet

router = routers.SimpleRouter()

router.register(
    'category',
    CategoryViewSet,
    base_name='category'
)
router.register(
    'note',
    NoteViewSet,
    base_name='note'
)
router.register(
    'public-note',
    PublicNoteViewSet,
    base_name='public-note'
)

# JWT
router.register(
    'api-token-auth',
    obtain_jwt_token,
    base_name='token-obtain'
)

urlpatterns = []
urlpatterns += router.urls
