from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import UserViewSet, PostViewSet
# from .views import PostList, PostDetail, UserList, UserDetail

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'', PostViewSet, basename='posts')

urlpatterns = router.urls