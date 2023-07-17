from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to the Portfolio portal"

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
