from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('users/<int:pk>/applications/', views.ApplicationList.as_view(), name='application_list'),
    path('users/<int:user_id>/applications/<int:pk>/', views.ApplicationDetail.as_view(), name='application_detail'),
    path('users/<int:pk>/interviews/', views.InterviewList.as_view(), name='interview_list'),
    path('users/<int:user_id>/interviews/<int:pk>/', views.InterviewDetail.as_view(), name='interview_detail'),
    path('users/<int:pk>/events/', views.EventList.as_view(), name='event_list'),
    path('users/<int:user_id>/events/<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
    path('users/<int:pk>/studies/', views.StudyList.as_view(), name='study_list'),
    path('users/<int:user_id>/studies/<int:pk>/', views.StudyDetail.as_view(), name='application_detail'),
    path('users/<int:pk>/histories/', views.HistoryList.as_view(), name='history_list'),
    path('users/<int:user_id>/histories/<int:pk>/', views.HistoryDetail.as_view(), name='history_detail')

]