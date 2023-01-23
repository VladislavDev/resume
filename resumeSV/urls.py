from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve 

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('exp/', include('exp.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(
            settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT
        )
    urlpatterns += staticfiles_urlpatterns()