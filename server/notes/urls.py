from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, NoteViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet, base_name='category')
router.register('note', NoteViewSet, base_name='note')

urlpatterns = [

]

urlpatterns += router.urls
