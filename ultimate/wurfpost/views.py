from django.shortcuts import render
from django.views.generic import ListView
from .models import Wurfpost

# Create your views here.
class WurfpostListView(ListView):
    model = Wurfpost
    context_object_name = 'wurfpost'
    ordering = ['datetime']
    paginate_by = 20
    
    
    def get_queryset(self):
        wurfpost =  super().get_queryset()
        return wurfpost