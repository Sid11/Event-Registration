from django.urls import path, include

urlpatterns = [
    path('', include('events.urls')),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]
