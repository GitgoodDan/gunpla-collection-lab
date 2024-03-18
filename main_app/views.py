from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Gunpla, Accessories


# Create your views here.

def home(request):
    return render(request, 'home.html')

def gunpla_index(request):
    gunpla = Gunpla.objects.all()
    return render(request, 'index.html',
    {
        'gunpla': gunpla
    }
)

def about(request):
    return render(request, 'about.html')

def gunpla_detail(request, gunpla_id):
    gunpla = Gunpla.objects.get(id=gunpla_id)
    return render(request, 'gunpla/detail.html', {'gunpla': gunpla})

class GunplaCreate(CreateView):
    model = Gunpla
    fields = '__all__'

class GunplaUpdate(UpdateView):
    model = Gunpla
    fields = ['series', 'description', 'grade', 'scale']

class GunplaRemove(DeleteView):
    model = Gunpla
    success_url = '/gunpla'

class AccessoriesList(ListView):
    model = Accessories

class AccessoryDetail(DetailView):
    model = Accessories

class AccessoryCreate(CreateView):
    model = Accessories
    fields = '__all__'

class AccessoryUpdate(UpdateView):
    model = Accessories
    fields = ['description']

class AccessoryRemove(DeleteView):
    model = Accessories
    success_url = '/accessories'