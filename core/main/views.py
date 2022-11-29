from django.shortcuts import render
from django.views.generic import ListView
from .models import Phone, SocMedia, HomeSliderActive, HomeSlider, HomeCategory, HomeSubCategory, SubCategProd
from django.template.defaulttags import register
# Create your views here.

@register.filter
def get_range(value):
    return range(value)
    
class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homeslider = HomeSlider.objects.all()
        homeslideractive = HomeSliderActive.objects.all()
        phone = Phone.objects.get()
        socmedia = SocMedia.objects.get()
        slidercount = HomeSlider.objects.all().count()
        homecateg = HomeCategory.objects.all()
        prod = HomeSubCategory.objects.all()
        return render(request, self.template_name, {'phone':phone, 'socmedia':socmedia, 'homeslideractive':homeslideractive, 'homeslider':homeslider, 'slidercount':slidercount, 'homecateg':homecateg, 'prod':prod})


class LoginListView(ListView):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

class Botas(ListView):
    template_name = 'botas.html'


    def get(self, request, id):
        botas = HomeSubCategory.objects.filter(pk=id)
        return render(request, self.template_name, {'id':id, 'botas':botas})