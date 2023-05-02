from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core.schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),

    path("i18n/", include("django.conf.urls.i18n")),
    path('rosetta/', include('rosetta.urls')),
    path('api/v1/user/', include('apps.users.urls'), name='users'),
    path('api/v1/canban/', include('apps.canban.urls'), name='canban'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('api/v1/social-auth/', include('apps.social_auth.urls'), name='social_auth'),

    # social auth
    re_path(r"^accounts/", include("allauth.urls"), name="socialaccount_signup"),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
urlpatterns += swagger_urlpatterns
# urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
