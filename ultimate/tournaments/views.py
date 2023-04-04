from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from bootstrap_datepicker_plus.widgets import DatePickerInput

#from .forms import NewTournamentForm
from .models import Tournament
# Create your views here.


class NewTournamentView(CreateView):
    model = Tournament
    fields = ['title', 'contact', 'contact_Mail', 'mail', 'link', 'start_Date', 'end_Date', 'location', 'type', 'mode', 'surface', 'gender', 'style', 'description']

    def get_form(self):
        form = super().get_form()
        form.fields['start_Date'].widget = DatePickerInput()
        form.fields['end_Date'].widget = DatePickerInput()
        return form

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'tournaments'
    ordering = ['start_Date']
    # paginate_by = 20

    def get_queryset(self):
        tournaments =  super().get_queryset()
        week = 0
        year = 0
        for tournament in tournaments:
            if week != tournament.start_Date.isocalendar()[1]:
                tournament.new_week = True
                week = tournament.start_Date.isocalendar()[1]
            if year != tournament.start_Date.isocalendar()[0]:
                tournament.new_year = True
                year = tournament.start_Date.isocalendar()[0]
        return tournaments

class TournamentDetailView(DetailView):
    model = Tournament

def approve(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    print(tournament.approved)
    tournament.approved = True
    print(tournament.approved)
    tournament.save()
    return redirect('tournaments')
    