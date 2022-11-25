from django.db import models

# Create your models here.


class Phone(models.Model):
    phone_number = models.TextField('Phone number')

    def __str__(self):
        return self.phone_number


class SocMedia(models.Model):
    img = models.ImageField('SocMedia img', upload_to='media')
    socmedia_url = models.URLField(max_length=300)


class HomeSliderActive(models.Model):
    name1 = models.CharField('HomeSlider name1', max_length=30)
    name2 = models.CharField('HomeSlider name2', max_length=30)
    about = models.TextField('HomeSlider about')
    img1 = models.ImageField('HomeSlider image1', upload_to='media')
    img2 = models.ImageField('HomeSlider image2', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSliderActive'
        verbose_name_plural = 'HomeSlidersActive'


class HomeSlider(models.Model):
    name1 = models.CharField('HomeSlider name1', max_length=30)
    name2 = models.CharField('HomeSlider name2', max_length=30)
    about = models.TextField('HomeSlider about')
    img1 = models.ImageField('HomeSlider image1', upload_to='media')
    img2 = models.ImageField('HomeSlider image2', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'


class HomeCategory(models.Model):
    name = models.CharField('HomeCategory name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeCategory'
        verbose_name_plural = 'HomeCategories'

class HomeSubCategory(models.Model):
    homecategory = models.ForeignKey(HomeCategory, on_delete=models.CASCADE, related_name='homecateg')
    name = models.CharField('HomeSubCategory name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeSubCategory'
        verbose_name_plural = 'HomeSubCategories'


    
class SubCategProd(models.Model):
    homesubcategory = models.ManyToManyField(HomeSubCategory, related_name='subitem')
    name = models.CharField('Item name', max_length=30)
    img = models.ImageField('Item image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategProd'
        verbose_name_plural = 'SubCategProds'

