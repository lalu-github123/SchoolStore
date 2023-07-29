from django.contrib import admin
from .models import Product,Category,Books

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20
admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class BooksAdmin(admin.ModelAdmin):
    list_display=['name','slug','author','price','stock',]
    list_editable=['price','stock',]
    prepopulated_fields={'slug':('name',)}
    list_per_page=20
admin.site.register(Books,BooksAdmin)



