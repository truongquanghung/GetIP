from django.shortcuts import redirect
from django.views import View
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("This is current Hippotech Server's IP: " + settings.IP)

class Update(View):
    def get(self, request, **kwargs):
        if settings.IP != kwargs['ip']:
            settings.IP = kwargs['ip']
        return redirect('/')