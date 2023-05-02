from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .generator import BothHttpAndHttpsSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Canban API",
        default_version="v1",
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)
# swagger_urlpatterns = [
#     re_path(
#         r"^swagger(?P<format>\.json|\.yaml)$",
#         schema_view.without_ui(cache_timeout=0),
#         name="schema-json",
#     ),
#     re_path(
#         "",
#         schema_view.with_ui("swagger", cache_timeout=0),
#         name="schema-swagger-ui",
#     ),
#     re_path(
#         r"^redoc/$",
#         schema_view.with_ui("redoc", cache_timeout=0),
#         name="schema-redoc",
#     ),
# ]
swagger_urlpatterns = [
    re_path(r"^doc(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("doc/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
