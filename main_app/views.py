from django.shortcuts import render

from .models import Gunpla

# gunpla = [
#     {'name': 'RX-78-02 Unleashed', 'series': 'Gundam', 'grade': 'Perfect Grade', 'scale': '1/60'},
#     {'name': 'RX-93 Nu Gundam', 'series': 'Gundam', 'grade': 'RG', 'scale': '1/144'},
#     {'name': 'Sinanju', 'series': 'Gundam Unicorn', 'grade': 'MG', 'scale': '1/100'},
#     {'name': 'Barbatos', 'series': 'Iron-Blooded Orphans', 'grade': 'MG', 'scale': '1/144'},
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def gunpla_index(request):
    models = Gunpla.objects.all()
    return render(request, 'index.html',
    {
        'gunpla': models
    }
)

def about(request):
    return render(request, 'about.html')

def gunpla_detail(request, gunpla_id):
    model = Gunpla.objects.get(id=gunpla_id)
    return render(request, 'gunpla/detail.html', {'gunpla': model})