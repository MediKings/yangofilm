from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('post.urls')),
    path('accounts/', include('accounts.urls')),
    path('', Home, name='home'),
    # path('back/', include('back.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
