from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Person, District,PoliceStation
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_districts(request):
    division_id = request.GET.get('division')
    districs = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'user/district_dropdown_list_options.html', {'districs': districs})

def load_policstation(request):
    district_id = request.GET.get('district')
    policstation=PoliceStation.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'user/policstation_dropdown_list_options.html', {'policstation' : policstation})

