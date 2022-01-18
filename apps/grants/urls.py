from rest_framework.routers import DefaultRouter

from apps.grants.views import CategoryAPIViewSet, LocationAPIViewSet, DisciplineAPIViewSet, GrantAPIViewSet

router = DefaultRouter()
router.register('grants', GrantAPIViewSet, basename='grants')
router.register('category', CategoryAPIViewSet, basename='category')
router.register('discipline', DisciplineAPIViewSet, basename='discipline')
router.register('location', LocationAPIViewSet, basename='location')

urlpatterns = router.urls
