from .views import ContactViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("contacts", ContactViewSet, basename="contact")

urlpatterns = []

urlpatterns += router.urls
