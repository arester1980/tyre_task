from django.http import HttpResponse
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

    def pars(self, tag):
        print('wORKS!!!')
        return 'works'
    #     with open(self, encoding="utf-8") as f:
    #         templates = yaml.safe_load(f)
    #         start = templates.find(tag)
    #         end = templates.find('</' + tag)
    #         value = templates[start:end]
    #         return value.split(">")[1]
    #
    # vendor = pars('items.yml', 'vendor')
    # model = pars('items.yml', 'model')
    # price = pars('items.yml', 'price')
    #
    # print(vendor)
    # print(model)
    # print(price)