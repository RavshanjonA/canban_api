from django.urls import path

from apps.canban.api_endpoints.Column.Column_List.views import ColumnListAPIView

app_name = 'canban'

urlpatterns = [
    path('columns/<int:board_id>/', ColumnListAPIView.as_view(), name='columns_by_board')
]
