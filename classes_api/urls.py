from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

app_name = 'classes_api'

urlpatterns = [
    path('', views.ClassroomList.as_view(), name='list'),
    path('<int:classroom_id>/', views.ClassroomDetail.as_view(), name='detail'),

    path('token/', TokenObtainPairView.as_view(), name='login'),

    path('create', views.ClassroomCreate.as_view(), name='classroom-create'),
    path('<int:classroom_id>/update/', views.ClassroomUpdate.as_view(), name='update'),
    path('<int:classroom_id>/delete/', views.ClassroomDelete.as_view(), name='delete'),
    path('create/', views.ClassroomCreate.as_view(), name='create'),
]
