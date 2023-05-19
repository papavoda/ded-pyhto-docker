from rest_framework.routers import SimpleRouter

from .views import PostListViewSet

router = SimpleRouter()
# router.register("users", UserViewSet, basename="users")

router.register("news", PostListViewSet, basename="news")
router.register("music", PostListViewSet, basename="music")
router.register("photo", PostListViewSet, basename="photo")
router.register("", PostListViewSet, basename="all")
urlpatterns = router.urls
