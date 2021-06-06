from django.conf.urls import url, include
from django.contrib import admin
from app.urls import router as app_router

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/', include(app_router.urls)),
]
