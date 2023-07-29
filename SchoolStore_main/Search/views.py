from django.shortcuts import render
from ProductApp.models import Product

# Create your views here.
def searchresult(request):
    products = Product.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(name__icontains=item_name)
    return render(request,'search.html',{'products':products})