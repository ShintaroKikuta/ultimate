import sys

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import MultipleObjectMixin, MultipleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView, FormMixin

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import NewTopicForm, NewBoardPostForm
from .models import Board, Topic, BoardPost

# def board_home(request):

#     boards = Board.objects.all()
#     return render(request, 'boards/boards.html', {'boards': boards})

class BoardsView(ListView):
    model = Board
    template_name = 'boards/boards.html'
    context_object_name = 'boards'


# def board_topics(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     return render(request, 'boards/topics.html', {'board': board})

class BoardTopicsView(DetailView):
    model = Board
    template_name = 'boards/topics.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'board'
    #ordering = ['-date_posted']


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = request.user

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = BoardPost.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            post.save()
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})


# class TopicCreateView(LoginRequiredMixin, CreateView):
#     model = Topic
#     fields = ['subject']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class TopicPostsView(LoginRequiredMixin, FormMixin, ListView):
    model = BoardPost
    form_class = NewBoardPostForm

    def get_queryset(self):
        return super(TopicPostsView, self).get_queryset().filter(topic = self.kwargs['topic_id'])

    paginate_by = 8
    template_name = 'boards/topic_old_cbv.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['created_at']




# def board_posts(request, board_id, topic_id):
#     posts_total = BoardPost.objects.filter(topic = topic_id).order_by('created_at')
#     page = request.GET.get('page', 1)
#     user = User.objects.first() #TODO

#     paginator = Paginator(posts_total, 8)
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     form = NewBoardPostForm()
#     return render(request, 'boards/topic.html', 
#         {'posts': posts, 'board': Board.objects.get(id=board_id), 'topic': Topic.objects.get(id=topic_id), 'form': form})

def new_boardpost(request, board_id, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    user = request.user
    if request.method == 'POST':
        form = NewBoardPostForm(request.POST)
        if form.is_valid():
            new_board_post = form.save(commit=False)
            new_board_post.topic = topic
            new_board_post.created_by = user
            new_board_post.created_at = None
            new_board_post.save()
            return redirect('topic_posts', board_id=board_id, topic_id=topic_id)
    #else:
        #form = NewBoardPostForm()
    return redirect('topic_posts', board_id=board_id, topic_id=topic_id)

#add messages at the top of the page