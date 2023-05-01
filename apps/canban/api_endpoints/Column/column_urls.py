from django.urls import path

from .Column_Create.views import ColumnCreateAPIView
from .Column_Destroy.views import ColumnDestroyAPIView
from .Column_List.views import ColumnListAPIView
from .Column_Update.views import ColumnUpdateAPIView

column_urlpatterns = [
    path('columns/<int:board_id>/', ColumnListAPIView.as_view(), name='columns_list_by_board'),
    path('columns/create/', ColumnCreateAPIView.as_view(), name='columns_create'),
    path('columns/destroy/<int:pk>/', ColumnDestroyAPIView.as_view(), name='columns_destroy'),
    path('columns/update/<int:pk>/', ColumnUpdateAPIView.as_view(), name='columns_update'),
]
