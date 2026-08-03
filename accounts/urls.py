from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet


router = DefaultRouter()

router.register("user-access", UserViewSet, basename="user-access")

urlpatterns = router.urls
