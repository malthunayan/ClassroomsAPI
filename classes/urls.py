from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.classroom_list, name='list'),
    path('<int:classroom_id>/', views.classroom_detail, name='detail'),

    path('create', views.classroom_create, name='classroom-create'),
    path('<int:classroom_id>/update/', views.classroom_update, name='update'),
    path('<int:classroom_id>/delete/', views.classroom_delete, name='delete'),
]
