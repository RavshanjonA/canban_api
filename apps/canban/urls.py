from django.urls import path

from apps.canban.api_endpoints.Board.Board_Create.views import BoardCreateAPIView
from apps.canban.api_endpoints.Board.Board_Destroy.views import BoardDestroyAPIView
from apps.canban.api_endpoints.Board.Board_List.views import BoardListAPIView
from apps.canban.api_endpoints.Board.Board_Update.views import BoardUpdateAPIView
from apps.canban.api_endpoints.Board.Board_Retrieve.views import BoardRetrieveAPIView

from apps.canban.api_endpoints.Column.Column_Create.views import ColumnCreateAPIView
from apps.canban.api_endpoints.Column.Column_Destroy.views import ColumnDestroyAPIView
from apps.canban.api_endpoints.Column.Column_List.views import ColumnListAPIView
from apps.canban.api_endpoints.Column.Column_Update.views import ColumnUpdateAPIView

app_name = 'canban'

urlpatterns = [
    path('boards/', BoardListAPIView.as_view(), name='boards_list'),
    path('boards/<int:pk>', BoardListAPIView.as_view(), name='boards_retrieve'),
    path('boards/create/', BoardCreateAPIView.as_view(), name='boards_create'),
    path('boards/destroy/<int:pk>/', BoardDestroyAPIView.as_view(), name='boards_destroy'),
    path('boards/update/<int:pk>/', BoardUpdateAPIView.as_view(), name='boards_update'),
    # ------------------------------------------------------------------------------------------
    path('columns/<int:board_id>/', ColumnListAPIView.as_view(), name='columns_list_by_board'),
    path('columns/create/', ColumnCreateAPIView.as_view(), name='columns_create'),
    path('columns/destroy/<int:pk>/', ColumnDestroyAPIView.as_view(), name='columns_destroy'),
    path('columns/update/<int:pk>/', ColumnUpdateAPIView.as_view(), name='columns_update'),
    # ------------------------------------------------------------------------------------------
]
