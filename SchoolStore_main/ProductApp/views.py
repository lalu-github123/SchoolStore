from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .models import Books,Category

# Create your views here.
def booksall(request,c_slug=None):

    c_page=None
    books_list=None

    if c_slug != None:
        c_page = get_object_or_404(Category,slug=c_slug)
        books_list = Books.objects.all().filter(category=c_page)
    else:
        books_list = Books.objects.all()

    paginator = Paginator(books_list,8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        books=paginator.page(page)
    except(EmptyPage,InvalidPage):
        books=paginator.page(paginator.num_pages)

    return render(request,"books.html",{'category':c_page,'books':books})
def categories(request):
    links = Category.objects.all()
    return render(request,"navbar.html",{'links':links})