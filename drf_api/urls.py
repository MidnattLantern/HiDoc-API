from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # logout route
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path('', include('art_acc.urls')),
    path('', include('project.urls')),
    path('', include('usr_comm.urls')),
    path('', include('watch_proj.urls')),
    path('', include('watch_art.urls')),
    path('', include('documentation.urls')),
]
