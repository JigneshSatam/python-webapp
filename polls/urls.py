from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
  # ex: /polls/
  path('', views.index, name='index'),
  # ex: /polls/3
  path('<int:question_id>/', views.detail, name='detail'),
  # ex: /polls/3/result
  path('<int:question_id>/result', views.results, name='result'),
  # ex: /polls/3/vote
  path('<int:question_id>/vote', views.vote, name='vote'),
]
