from django.contrib import admin
from .models import Phone, SocMedia, HomeSlider, HomeSliderActive, HomeCategory, HomeSubCategory, SubCategProd
# Register your models here.


admin.site.register(Phone)
admin.site.register(SocMedia)
admin.site.register(HomeSliderActive)
admin.site.register(HomeSlider)
admin.site.register(HomeCategory)
admin.site.register(HomeSubCategory)
admin.site.register(SubCategProd)
