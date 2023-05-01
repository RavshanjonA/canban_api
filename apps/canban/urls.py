from apps.canban.api_endpoints.Board.board_urls import board_urlpatterns
from apps.canban.api_endpoints.Column.column_urls import column_urlpatterns
from apps.canban.api_endpoints.Subtask.subtask_urls import subtask_urlpatterns
from apps.canban.api_endpoints.Task.task_urls import task_urlpatterns

app_name = 'canban'

urlpatterns = [

]

urlpatterns += board_urlpatterns + column_urlpatterns + task_urlpatterns + subtask_urlpatterns
