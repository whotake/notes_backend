from rest_framework import routers
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from server.users.views import UserViewSet

router = routers.SimpleRouter()

router.register(
    'user',
    UserViewSet,
    base_name='user',
)

urlpatterns = [
    # JWT:
    url(r'^api-token-auth', obtain_jwt_token, name='api-token-auth'),
]

urlpatterns += router.urls
