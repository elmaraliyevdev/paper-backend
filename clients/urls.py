from .views import ClientViewSet
from rest_framework.routers import DefaultRouter

app_name = 'clients'

router = DefaultRouter()

router.register('', ClientViewSet, basename='clients')

urlpatterns = router.urls
