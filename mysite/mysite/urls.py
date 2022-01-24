from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls'), name='index'),
    path('admin/', admin.site.urls),
]
