from .views import ProjectViewSet
from rest_framework.routers import DefaultRouter

app_name = 'projects'

router = DefaultRouter()

router.register('', ProjectViewSet, basename='projects')

urlpatterns = router.urls
