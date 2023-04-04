from django.urls import path, re_path
from . import views


urlpatterns = [
	path('', views.BoardsView.as_view(), name= "board-home"),
    # path('<pk>/', views.board_topics. name='board_topics'),
    re_path(r'^(?P<pk>\d+)/$', views.BoardTopicsView.as_view(), name='board_topics'),
    #re_path(r'^(?P<pk>\d+)/newold/$', views.new_topic, name='new_topic'),
    re_path(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    path('<board_id>/<topic_id>/', views.TopicPostsView.as_view(), name='topic_posts'),
    path('<board_id>/<topic_id>/new/', views.new_boardpost, name='new_boardpost')
]
