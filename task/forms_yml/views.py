from django.http import HttpResponse, HttpResponseRedirect
from .models import Tyre, Incoming
from django.views.generic import ListView, DetailView
import yaml


def index(request):
    return HttpResponse('Hello, world. You\'re at the polls index.')


class PostListView(ListView):
    queryset = Tyre.objects.all()
    context_object_name = 'items'
    template_name = 'task/list.html'


class FileView(DetailView):
    model = Incoming
    template_name = 'task/detail.html'
    pk_url_kwarg = 'id'


def create(request):
    if request.method == "POST":
        tyre = Incoming()
        tyre.vendor = request.POST.get("vendor")
        tyre.model = request.POST.get("model")
        tyre.price = request.POST.get("price")
        tyre.save()
    return HttpResponseRedirect("/")