from django.urls import path
from watch_art import views

urlpatterns = [
    path('watch-artists/', views.WatchArtistList.as_view()),
    path('watch-artists/<int:pk>/', views.WatchArtistDetail.as_view()),
]