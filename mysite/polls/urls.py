from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
