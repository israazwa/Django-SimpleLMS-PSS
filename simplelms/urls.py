from django.contrib import admin   # ⬅️ INI YANG KURANG
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('silk/', include('silk.urls', namespace='silk')),
    path('', include('core.urls')),
]