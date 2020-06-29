from .models import Tyre
from .templates import worker
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def start(request):
    return render(request, 'forms_yml/index.html')
    # vendor = worker.pars('task/items.yml', 'vendor')
    # model = worker.pars('task/items.yml', 'model')
    # price = worker.pars('task/items.yml', 'price')


def list_tyre(request):
    tyres = Tyre.objects.all()
    return render(request, 'forms_yml/list.html', {'tyres': tyres})


def upload_file(request):
    if request.method == 'POST':
        f = request.FILES['upload']
        fs = FileSystemStorage()
        name = fs.save(f.name, f)
        url = fs.url(name)
        vendor = worker.pars(f'media/{name}', 'vendor')
        model = worker.pars(f'media/{name}', 'model')
        price = worker.pars(f'media/{name}', 'price')
        return render(request, 'forms_yml/result.html', {'vendor': vendor, 'model': model, 'price': price})