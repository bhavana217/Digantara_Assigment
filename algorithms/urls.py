from django.urls import path
from .views import binary_search_view, quick_sort_view, bfs_view, AlgorithmLogListView

urlpatterns = [
    path('binary_search/', binary_search_view),
    path('quick_sort/', quick_sort_view),
    path('bfs/', bfs_view),
    path('logs/', AlgorithmLogListView.as_view(), name='algorithm-logs'),
]