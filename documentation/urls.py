from django.urls import path
from documentation import views

urlpatterns = [
    path('documentations/', views.DocumentationList.as_view()),
    path('documentations/<int:pk>/', views.DocumentationDetail.as_view())
]
