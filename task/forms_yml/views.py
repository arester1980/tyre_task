from django.http import HttpResponse
from .models import Tyre
from .forms import UploadFileForm
from django.views.generic import ListView
from .templates import worker
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def index(request):
    vendor = worker.pars('task/items.yml', 'vendor')
    model = worker.pars('task/items.yml', 'model')
    price = worker.pars('task/items.yml', 'price')
    return HttpResponse('Vendor: {}\nModel: {}\nPrice: {}'.format(vendor, model, price))

def tyre_new(request):
    if request.method == "POST":
        vendor = worker.pars('files', 'vendor')
        model = worker.pars('files', 'model')
        price = worker.pars('files', 'price')
        print(vendor)
        print(model)
        print(price)
        return render('list')
        # return HttpResponse('Vendor: {}\nModel: {}\nPrice: {}'.format(vendor, model, price))

def upload_file(request):
    if request.method == 'POST':
        f = request.FILES['upload']
        fs = FileSystemStorage()
        name = fs.save(f.name, f)
        url = fs.url(name)
        print(url)
        vendor = worker.pars(name, 'vendor')
        model = worker.pars(name, 'model')
        price = worker.pars(name, 'price')
        print(vendor)
        print(model)
        print(price)
    return render(request, template_name='task/list.html')

class PostListView(ListView):
    queryset = Tyre.objects.all()
    context_object_name = 'items'
    template_name = 'task/list.html'