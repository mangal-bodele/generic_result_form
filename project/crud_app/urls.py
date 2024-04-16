from django.urls import path
from .views import *

urlpatterns = [
    path('create/', Result_Create.as_view(),name="create_url"),
    path('list/', Result_List.as_view(),name="list_url"),
    path('detail/<int:pk>/', Result_Detail.as_view(),name="detail_url"),
    path('update/<int:pk>/', Result_Update.as_view(),name="update_url"),
    path('delete/<int:pk>/', Result_Delete.as_view(),name="delete_url")
]