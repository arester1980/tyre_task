from .models import Tyre
from .templates import worker
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import TyreForm


def start(request):
    return render(request, 'forms_yml/index.html')


def list_tyre(request):
    tyres = Tyre.objects.all()
    return render(request, 'forms_yml/list.html', {'tyres': tyres})

def upload_file(request):
    if request.method == 'POST':
        f = request.FILES['upload']
        fs = FileSystemStorage()
        name = fs.save(f.name, f)
        context = {
            'vendor': worker.pars(f'media/{name}', 'vendor'),
            'model': worker.pars(f'media/{name}', 'model'),
            'price': worker.pars(f'media/{name}', 'price'),
            'currency': worker.pars(f'media/{name}', 'currency')
        }
        form = TyreForm()
        if form.is_valid():
            form.save()
        return render(request, 'forms_yml/result.html', context)