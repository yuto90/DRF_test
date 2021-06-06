from rest_framework import routers
from .views import UserViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
