from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)

    #def get_url(self):
       # return reverse('Eapp1:procatdetail',args=[self.category.slug,self.slug])

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
       return reverse('ProductApp:books_by_category',args=[self.slug])
class Books(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    author=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()

    class Meta:
        ordering=('name',)
        verbose_name='book'
        verbose_name_plural='books'

    def __str__(self):
        return '{}'.format(self.name)

    #def get_url(self):
        #return reverse('Eapp1:procatdetail',args=[self.category.slug,self.slug])
