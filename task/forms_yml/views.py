from .models import Tyre
from .templates import worker
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import TyreForm, VendorForm


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
        return render(request, 'forms_yml/result.html', context)

def save(request):
    form_tyre = TyreForm()
    context = {
        'form_tyre': form_tyre,
        'vendor': 'SS'
    }
    if request.method == 'POST':
        form_tyre = TyreForm(request.POST)
        print(form_tyre)
        if form_tyre.is_valid():
            form_tyre.save()
            return redirect('list')
        else:
            print('Error')

    return render(request, 'forms_yml/save.html', context)