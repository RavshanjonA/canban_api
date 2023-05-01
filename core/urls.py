from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from core.schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/user/', include('apps.users.urls'), name='users'),
    # path('canban/', include('apps.canban.urls'), name='canban'),

    path("i18n/", include("django.conf.urls.i18n")),
    path('api/v1/canban/', include('apps.canban.urls'), name='canban'),
    path('api/v1/social-auth/', include('apps.social_auth.urls'), name='social_auth'),

    # social auth
    re_path(r"^accounts/", include("allauth.urls"), name="socialaccount_signup"),
]
urlpatterns += swagger_urlpatterns
# urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
