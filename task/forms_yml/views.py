from django.http import HttpResponse
from .models import Tyre
from django.views.generic import ListView
from .templates import worker
from django.shortcuts import render


def index(request):
    vendor = worker.pars('task/items.yml', 'vendor')
    model = worker.pars('task/items.yml', 'model')
    price = worker.pars('task/items.yml', 'price')
    return HttpResponse('Vendor: {}\nModel: {}\nPrice: {}'.format(vendor, model, price))

def tyre_new(request):
    if request.method == "POST":
        print(request.f)
        vendor = worker.pars('files', 'vendor')
        model = worker.pars('files', 'model')
        price = worker.pars('files', 'price')
        print(vendor)
        print(model)
        return render('list')
        # return HttpResponse('Vendor: {}\nModel: {}\nPrice: {}'.format(vendor, model, price))


class PostListView(ListView):
    queryset = Tyre.objects.all()
    context_object_name = 'items'
    template_name = 'task/list.html'