from django.urls import path
from usr_comm import views

urlpatterns = [
    path('user-comments/', views.UserCommentList.as_view()),
    path('user-comments/<int:pk>', views.UserCommentDetail.as_view()),
]
