from django.urls import path, include

from . import views


urlpatterns = [
    path('<int:puzzle_pk>/', views.index, name='index'),
    path('<int:puzzle_pk>/answer/', views.answer, name='answer'),
]