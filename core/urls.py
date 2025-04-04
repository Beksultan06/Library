from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.yasg import urlpatterns_yasg


# Основные маршруты (не зависят от мультиязычности)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(urlpatterns_yasg)),  # ✅ Swagger (yasg)
]

# Маршруты, зависящие от языка (i18n)
urlpatterns += i18n_patterns(
    path('api/v1/users/', include('app.users.urls')),
    path('api/v1/afisha/', include('app.afisha.urls')),
    path('api/v1/services/', include('app.services.urls')),
    path('api/v1/banner/', include('app.page_for_readers.urls')),
    path('api/v1/Graphic_work/', include('app.page_for_readers.urls')),
    path('api/v1/professional_activity/', include('app.professional_activity.urls')),
    path('api/v1/stats/', include('app.activity.urls')),
    path('api/v1/project/', include('app.projects.urls')),
    path('api/v1/base/', include('app.base.urls')),
    path("api/v1/news/", include("app.news.urls")),
    path("api/v1/about_library/", include("app.about_library.urls")),
    path("api/v1/supports/", include("app.supports.urls")),
)

# Раздача статических и медиа-файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)