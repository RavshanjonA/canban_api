from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core.schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/v1/user/', include('apps.users.urls'), name='users'),
    path('api/v1/canban/', include('apps.canban.urls'), name='canban'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
urlpatterns += swagger_urlpatterns
# urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
