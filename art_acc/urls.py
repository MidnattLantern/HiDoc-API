from django.urls import path
from art_acc import views

urlpatterns = [
    path('art-accounts/', views.ArtAccountList.as_view()),
]