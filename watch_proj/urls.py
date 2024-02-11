from django.urls import path
from watch_proj import views

urlpatterns = [
    path('watch-projects/', views.WatchProjectList.as_view()),
    path('watch-projects/<int:pk>', views.WatchProjectDetail.as_view()),
]
