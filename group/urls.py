from django.urls import path, include

from .views import *

urlpatterns = [   
    path("", GroupListView.as_view(), name="group_all"),
    path('<int:pk>/detail', GroupDetailView.as_view(), name='group_detail'),
    path('new/', GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
    
    path("grid/<int:pk>/detail/", GridGroupDetailView.as_view(), name="gridgroup"),
]
