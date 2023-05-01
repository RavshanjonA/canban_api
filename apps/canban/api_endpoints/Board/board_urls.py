from django.urls import path

from .Board_Create.views import BoardCreateAPIView
from .Board_Destroy.views import BoardDestroyAPIView
from .Board_List.views import BoardListAPIView
from .Board_Retrieve.views import BoardRetrieveAPIView
from .Board_Update.views import BoardUpdateAPIView

board_urlpatterns = [
    path('boards/', BoardListAPIView.as_view(), name='boards_list'),
    path('boards/<int:pk>', BoardRetrieveAPIView.as_view(), name='boards_retrieve'),
    path('boards/create/', BoardCreateAPIView.as_view(), name='boards_create'),
    path('boards/destroy/<int:pk>/', BoardDestroyAPIView.as_view(), name='boards_destroy'),
    path('boards/update/<int:pk>/', BoardUpdateAPIView.as_view(), name='boards_update'),
]
