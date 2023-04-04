from django.urls import path, re_path
from . import views


urlpatterns = [
    path('new/', views.NewTournamentView.as_view(), name='new-tournament'),
    path('', views.TournamentListView.as_view(), name='tournaments'),
    path('<int:pk>/', views.TournamentDetailView.as_view(), name="tournament-detail"),
    path('approve/<int:tournament_id>', views.approve, name="tournament-approve"),
]